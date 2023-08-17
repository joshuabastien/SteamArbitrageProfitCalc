import requests
import tkinter as tk
from tkinter import ttk
from tkinter import *

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
    # This function has been adjusted to return data instead of printing it.
    output_data = []

    # Get floats of CAD values
    lowest_price_cad_value = float(cad_price_data.get('lowest_price', 'N/A').replace("CDN$ ", "")) if cad_price_data.get('lowest_price', 'N/A') != 'N/A' else None
    median_price_cad_value = float(cad_price_data.get('median_price', 'N/A').replace("CDN$ ", "")) if cad_price_data.get('median_price', 'N/A') != 'N/A' else None

    # Get floats of Lira values
    lowest_price_lira_value = float(lira_price_data.get('lowest_price', 'N/A').replace(" TL", "").replace(".", "").replace(",", ".")) if lira_price_data.get('lowest_price', 'N/A') != 'N/A' else None
    median_price_lira_value = float(lira_price_data.get('median_price', 'N/A').replace(" TL", "").replace(".", "").replace(",", ".")) if lira_price_data.get('median_price', 'N/A') != 'N/A' else None

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
    output_data.append(divider)
    output_data.append(f"Details for: {market_hash_name}".center(50))
    output_data.append(divider)

    # Skinport details
    output_data.append(f"{'Skinport Price (CAD)':<40}: ${skinport_price_cad:.2f}")
    output_data.append(divider)

    # Steam Lowest Price details
    output_data.append("Steam Lowest Price Details".center(50))
    output_data.append(f"{'Price (Lira)':<40}: {lowest_price_lira_value:.2f}₺")
    output_data.append(f"{'Price (CAD)':<40}: ${lowest_price_cad_value:.2f}")
    output_data.append(f"{'Adjusted Price (CAD)':<40}: ${adjusted_lowest_price_cad:.2f}")
    output_data.append(f"{'Ratio':<40}: {ratio_lowest:.2f}")
    output_data.append(f"{'Difference (CAD)':<40}: ${diff_lowest:.2f}")
    output_data.append(divider)

    # Steam Median Price details
    output_data.append("Steam Median Price Details".center(50))
    output_data.append(f"{'Price (Lira)':<40}: {median_price_lira_value:.2f}₺" if median_price_lira_value is not None else "N/A")
    output_data.append(f"{'Price (CAD)':<40}: ${median_price_cad_value:.2f}" if median_price_cad_value is not None else "N/A")
    output_data.append(f"{'Adjusted Price (CAD)':<40}: ${adjusted_median_price_cad:.2f}" if adjusted_median_price_cad is not None else "N/A")
    output_data.append(f"{'Ratio':<40}: {ratio_median:.2f}" if ratio_median is not None else "N/A")
    output_data.append(f"{'Difference (CAD)':<40}: ${diff_median:.2f}" if diff_median is not None else "N/A")
    output_data.append(divider)

    # Volume
    output_data.append(f"{'Volume':<40}: {cad_price_data.get('volume', 'N/A')}")
    output_data.append(divider)

    return output_data

def on_submit(stattrak_var, knife_glove_var, weapon_type_entry, skin_name_entry, cond_list_entry, skinport_price_entry):
    # Getting the values from the entry boxes
    stattrak = stattrak_var.get().strip().lower() == 'y'
    knife = knife_glove_var.get().strip().lower() == 'y'
    weapon_type = weapon_type_entry.get().strip()
    skin_name = skin_name_entry.get().strip()
    item_condition = cond_list_entry.get().strip()
    try:
        skinport_price_cad = float(skinport_price_entry.get().strip().replace("$", ""))
    except ValueError:
        show_output_window("Invalid Skinport price input.")
        return

    # The following section is adapted from your original main function
    app_id = 730  # CS:GO's App ID

    if stattrak and knife:
        market_hash_name = "★ " + f"StatTrak™ {weapon_type} | {skin_name} ({item_condition})"
    elif stattrak:
        market_hash_name = f"StatTrak™ {weapon_type} | {skin_name} ({item_condition})"
    elif knife:
        market_hash_name = "★ " + f"{weapon_type} | {skin_name} ({item_condition})"
    else:
        market_hash_name = f"{weapon_type} | {skin_name} ({item_condition})"
    
    cad_price = get_steam_market_price_cad(app_id, market_hash_name)
    lira_price = get_steam_market_price_lira(app_id, market_hash_name)

    if cad_price and lira_price:
        output_data = []
        try: 
            output_data.extend(display_price_info(market_hash_name, cad_price, lira_price, skinport_price_cad))
        except TypeError:
            show_output_window(market_hash_name, "Item too valuable to be sold on steam ($2000 limit).")
            return
        show_output_window(market_hash_name, "\n".join(output_data))
    else:
        show_output_window(market_hash_name, "Couldn't fetch the price.")

    # Clearing the text fields
    stattrak_var.set('n')  # Reset the radio button to 'No' after processing
    knife_glove_var.set('n')
    weapon_type_entry.delete(0, tk.END)
    skin_name_entry.delete(0, tk.END)
    cond_list_entry.set("Factory New")
    skinport_price_entry.delete(0, tk.END)

def show_output_window(market_hash_name, output_text):
    output_window = tk.Toplevel()
    output_window.title(f"{market_hash_name}")

    # Use Text widget for better formatting
    # Adjust the height and width as needed
    text_widget = tk.Text(output_window, wrap=tk.WORD, height=30, width=70)
    text_widget.pack(padx=20, pady=20)

    # Configure the 'center' tag to align text to the center
    text_widget.tag_configure('center', justify='center')

    text_widget.insert(tk.END, output_text, 'center')  # Apply the 'center' tag to the inserted text

    # Disable editing for the text widget
    text_widget.config(state=tk.DISABLED)

def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Steam Market Price Checker")

    # StatTrak Radiobuttons
    ttk.Label(window, text="Is the weapon a StatTrak™ weapon?").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    stattrak_var = tk.StringVar(value='n')
    ttk.Radiobutton(window, text="Yes", variable=stattrak_var, value="y").grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
    ttk.Radiobutton(window, text="No", variable=stattrak_var, value="n").grid(row=0, column=1, sticky=tk.E, padx=10, pady=5)

    # Knife or Glove Radiobuttons
    ttk.Label(window, text="Is the weapon a Knife or Glove?").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
    knife_glove_var = tk.StringVar(value='n')
    ttk.Radiobutton(window, text="Yes", variable=knife_glove_var, value="y").grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
    ttk.Radiobutton(window, text="No", variable=knife_glove_var, value="n").grid(row=1, column=1, sticky=tk.E, padx=10, pady=5)

    ttk.Label(window, text="Enter the weapon type:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    weapon_type_entry = ttk.Entry(window)
    weapon_type_entry.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(window, text="Enter the skin name:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    skin_name_entry = ttk.Entry(window)
    skin_name_entry.grid(row=3, column=1, padx=10, pady=5)

    # Condition drop down menu
    ttk.Label(window, text="Choose the condition of the item:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
    cond_list_entry = StringVar(window)
    cond_list_entry.set("Factory New")
    item_condition_entry = ttk.OptionMenu(window, cond_list_entry, "Factory New", "Factory New", "Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scarred")
    item_condition_entry.grid(row=4, column=1, padx=10, pady=5)

    ttk.Label(window, text="Enter the Skinport price in CAD:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
    skinport_price_entry = ttk.Entry(window)
    skinport_price_entry.grid(row=5, column=1, padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(window, text="Submit", command=lambda: on_submit(stattrak_var, knife_glove_var, weapon_type_entry, skin_name_entry, cond_list_entry, skinport_price_entry))
    submit_button.grid(row=6, column=0, columnspan=2, pady=15)

    # Start the GUI loop
    window.mainloop()

if __name__ == "__main__":
    create_gui()
