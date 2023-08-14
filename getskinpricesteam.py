import requests

def get_steam_market_price(app_id, market_hash_name):
    base_url = "https://steamcommunity.com/market/priceoverview/"
    params = {
        'country': 'US',
        'currency': 1,
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

def convert_to_lira(cad_price, exchange_rate):
    try:
        # Remove the dollar sign and convert to float
        numeric_price = float(cad_price.replace("$", ""))
        return numeric_price * exchange_rate
    except ValueError:
        return None
    
def convert_to_cad(usd_price):
    conversion_rate = 1.34  # 1 USD to CAD
    try:
        numeric_price = float(usd_price.replace("$", ""))
        return "${:.2f}".format(numeric_price * conversion_rate)  # Return as string with dollar sign
    except ValueError:
        return None

def display_price_info(market_hash_name, price_data, exchange_rate, skinport_price_cad):
    item_name = market_hash_name
    lowest_price_usd = price_data.get('lowest_price', 'N/A')
    median_price_usd = price_data.get('median_price', 'N/A')

    # Convert USD to CAD
    lowest_price_cad_value = float(lowest_price_usd.replace("$", "").replace(",", "")) * 1.34 if lowest_price_usd != 'N/A' else None
    median_price_cad_value = float(median_price_usd.replace("$", "").replace(",", "")) * 1.34 if median_price_usd != 'N/A' else None

    # Convert CAD prices to Lira
    lowest_price_lira = lowest_price_cad_value * exchange_rate if lowest_price_cad_value is not None else None
    median_price_lira = median_price_cad_value * exchange_rate if median_price_cad_value is not None else None

    # Adjusted calculations for lowest price
    adjusted_lowest_price_cad = lowest_price_cad_value / 1.15 if lowest_price_cad_value is not None else None
    diff_lowest = adjusted_lowest_price_cad - skinport_price_cad if adjusted_lowest_price_cad is not None else None
    ratio_lowest = adjusted_lowest_price_cad / skinport_price_cad if adjusted_lowest_price_cad is not None else None

    # Adjusted calculations for median price
    adjusted_median_price_cad = median_price_cad_value / 1.15 if median_price_cad_value is not None else None
    diff_median = adjusted_median_price_cad - skinport_price_cad if adjusted_median_price_cad is not None else None
    ratio_median = adjusted_median_price_cad / skinport_price_cad if adjusted_median_price_cad is not None else None

    # Enhanced Display:
    divider = "-" * 50  # Horizontal divider

    print(divider)
    print(f"Details for: {item_name}".center(50))
    print(divider)

    # Skinport details
    print(f"{'Skinport Price (CAD)':<40}: ${skinport_price_cad:.2f}")
    print(divider)

    # Steam Lowest Price details
    print("Steam Lowest Price Details".center(50))
    print(f"{'Price (Lira)':<40}: {lowest_price_lira:.2f}₺")
    print(f"{'Price (CAD)':<40}: ${lowest_price_cad_value:.2f}")
    print(f"{'Adjusted Price (CAD)':<40}: ${adjusted_lowest_price_cad:.2f}")
    print(f"{'Ratio':<40}: {ratio_lowest:.2f}")
    print(f"{'Difference (CAD)':<40}: ${diff_lowest:.2f}")
    print(divider)

    # Steam Median Price details
    print("Steam Median Price Details".center(50))
    print(f"{'Price (Lira)':<40}: {median_price_lira:.2f}₺" if median_price_lira is not None else "N/A")
    print(f"{'Price (CAD)':<40}: ${median_price_cad_value:.2f}" if median_price_cad_value is not None else "N/A")
    print(f"{'Adjusted Price (CAD)':<40}: ${adjusted_median_price_cad:.2f}" if adjusted_median_price_cad is not None else "N/A")
    print(f"{'Ratio':<40}: {ratio_median:.2f}" if ratio_median is not None else "N/A")
    print(f"{'Difference (CAD)':<40}: ${diff_median:.2f}" if diff_median is not None else "N/A")
    print(divider)

    # Volume
    print(f"{'Volume':<40}: {price_data.get('volume', 'N/A')}")
    print(divider)

if __name__ == "__main__":
    app_id = 730  # CS:GO's App ID
    
    # Input the gun type, skin name, and condition separately
    print("Enter the gun type (e.g., 'P250'):")
    gun_type = input().strip()
    
    print("Enter the skin name (e.g., 'Apep's Curse'):")
    skin_name = input().strip()

    print("Enter the condition of the item (e.g., 'Battle-Scarred'):")
    item_condition = input().strip()

    # Concatenate the gun type, skin name, and condition
    market_hash_name = f"{gun_type} | {skin_name} ({item_condition})"

    print("Enter the Skinport price in CAD (e.g., CA$59.71):")
    try:
        skinport_price_cad = float(input().strip().replace("CA$", "").replace(",", ""))
    except ValueError:
        print("Invalid input. Please enter a valid price in format: CA$59.71")
        exit()

    exchange_rate = 19.99  # CAD to Lira

    price = get_steam_market_price(app_id, market_hash_name)
    if price:
        display_price_info(market_hash_name, price, exchange_rate, skinport_price_cad)
    else:
        print("Couldn't fetch the price.")
