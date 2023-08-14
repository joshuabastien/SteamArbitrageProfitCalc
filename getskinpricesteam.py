import requests

def get_steam_market_price_cad(app_id, market_hash_name):
    base_url = "https://steamcommunity.com/market/priceoverview/"
    params = {
        'country': 'CA',
        'currency': 20,
        'appid': app_id,
        'market_hash_name': market_hash_name
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        if data.get('success'):
            return data
        else:
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    
def get_steam_market_price_lira(app_id, market_hash_name):
    base_url = "https://steamcommunity.com/market/priceoverview/"
    params = {
        'country': 'TR',
        'currency': 17,
        'appid': app_id,
        'market_hash_name': market_hash_name
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        if data.get('success'):
            return data
        else:
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def display_price_info(market_hash_name, cad_price_data, lira_price_data, skinport_price_cad):

    # Get floats of cad values
    lowest_price_cad_value = float(cad_price_data.get('lowest_price', 'N/A').replace("CDN$ ", "")) if cad_price_data.get('lowest_price', 'N/A') != 'N/A' else None
    median_price_cad_value = float(cad_price_data.get('median_price', 'N/A').replace("CDN$ ", "")) if cad_price_data.get('median_price', 'N/A') != 'N/A' else None

    # Get floats of lira values
    lowest_price_lira_value = float(lira_price_data.get('lowest_price', 'N/A').replace(" TL", "").replace(".", "").replace("," , ".")) if lira_price_data.get('lowest_price', 'N/A') != 'N/A' else None
    median_price_lira_value = float(lira_price_data.get('median_price', 'N/A').replace(" TL", "").replace(".", "").replace("," , ".")) if lira_price_data.get('median_price', 'N/A') != 'N/A' else None

    # Adjusted calculations for lowest price
    adjusted_lowest_price_cad = lowest_price_cad_value / 1.15 - 0.01 if lowest_price_cad_value is not None else None
    diff_lowest = adjusted_lowest_price_cad - skinport_price_cad if adjusted_lowest_price_cad is not None else None
    ratio_lowest = adjusted_lowest_price_cad / skinport_price_cad if adjusted_lowest_price_cad is not None else None

    # Adjusted calculations for median price
    adjusted_median_price_cad = median_price_cad_value / 1.15 - 0.01 if median_price_cad_value is not None else None
    diff_median = adjusted_median_price_cad - skinport_price_cad if adjusted_median_price_cad is not None else None
    ratio_median = adjusted_median_price_cad / skinport_price_cad if adjusted_median_price_cad is not None else None

    # Enhanced Display:
    divider = "-" * 50  # Horizontal divider

    print(divider)
    print(f"Details for: {market_hash_name}".center(50))
    print(divider)

    # Skinport details
    print(f"{'Skinport Price (CAD)':<40}: ${skinport_price_cad:.2f}")
    print(divider)

    # Steam Lowest Price details
    print("Steam Lowest Price Details".center(50))
    print(f"{'Price (Lira)':<40}: {lowest_price_lira_value:.2f}₺")
    print(f"{'Price (CAD)':<40}: ${lowest_price_cad_value:.2f}")
    print(f"{'Adjusted Price (CAD)':<40}: ${adjusted_lowest_price_cad:.2f}")
    print(f"{'Ratio':<40}: {ratio_lowest:.2f}")
    print(f"{'Difference (CAD)':<40}: ${diff_lowest:.2f}")
    print(divider)

    # Steam Median Price details
    print("Steam Median Price Details".center(50))
    print(f"{'Price (Lira)':<40}: {median_price_lira_value:.2f}₺" if median_price_lira_value is not None else "N/A")
    print(f"{'Price (CAD)':<40}: ${median_price_cad_value:.2f}" if median_price_cad_value is not None else "N/A")
    print(f"{'Adjusted Price (CAD)':<40}: ${adjusted_median_price_cad:.2f}" if adjusted_median_price_cad is not None else "N/A")
    print(f"{'Ratio':<40}: {ratio_median:.2f}" if ratio_median is not None else "N/A")
    print(f"{'Difference (CAD)':<40}: ${diff_median:.2f}" if diff_median is not None else "N/A")
    print(divider)

    # Volume
    print(f"{'Volume':<40}: {cad_price_data.get('volume', 'N/A')}")
    print(divider)

if __name__ == "__main__":
    app_id = 730  # CS:GO's App ID

    print("Is the weapon a StatTrak™ weapon? (y/n)")
    stattrak = True if input().strip() == "y" else False

    print("Is the weapon a Knife or Glove? (y/n)")
    knife = True if input().strip() == "y" else False
    
    # Input the weapon type, skin name, and condition separately
    print("Enter the weapon type (e.g., P250 or Flip Knife):")
    weapon_type = input().strip()
    
    print("Enter the skin name (e.g., Apep's Curse):")
    skin_name = input().strip()

    print("Enter the condition of the item (e.g., Battle-Scarred or bs):")
    temp = input().strip()
    match temp:
        case "fn":
            item_condition = "Factory New"
        case "mw":
            item_condition = "Minimal Wear"
        case "ft":
            item_condition = "Field-Tested"
        case "ww":
            item_condition = "Well-Worn"
        case "bs":
            item_condition = "Battle-Scarred"
        case _:
            item_condition = temp

    # Concatenate the gun type, skin name, and condition
    if stattrak and knife:
        market_hash_name = "★ " + f"StatTrak™ {weapon_type} | {skin_name} ({item_condition})"
    elif stattrak:
        market_hash_name = f"StatTrak™ {weapon_type} | {skin_name} ({item_condition})"
    elif knife:
        market_hash_name = "★ " + f"{weapon_type} | {skin_name} ({item_condition})"
    else:
        market_hash_name = f"{weapon_type} | {skin_name} ({item_condition})"

    print("Enter the Skinport price in CAD (e.g., $59.71 or 59.71):")
    try:
        skinport_price_cad = float(input().strip().replace("$", ""))
    except ValueError:
        print("Invalid input. Please enter a valid price in format: CA$59.71")
        exit()

    cad_price = get_steam_market_price_cad(app_id, market_hash_name)
    lira_price = get_steam_market_price_lira(app_id, market_hash_name)

    if cad_price and lira_price:
        display_price_info(market_hash_name, cad_price, lira_price, skinport_price_cad)
    else:
        print("Couldn't fetch the price.")

