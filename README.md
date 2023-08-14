# Steam Market Price Fetcher & Converter

## Description:
This program fetches the market price of CS:GO in-game items from the Steam Market and provides a detailed overview of the item price, converting it to different currencies and comparing it with another market price from Skinport. It can be especially useful for traders or users who want to get an idea of the comparative price of their items in different markets.

## Features:
- Fetches the lowest and median price of a CS:GO item from Steam Market.
- Converts the USD price to CAD.
- Converts the CAD price to Lira.
- Provides an adjusted price (after removing a 15% fee) to compare with Skinport.
- Displays a comprehensive breakdown of the prices, ratio, and difference.

## Prerequisites:
To use this script, ensure you have:
1. Python installed on your system.
2. The `requests` library installed. If not, install it using `pip install requests`.

## How to Use:

1. Clone/Download the script to your system.
2. Open the terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using `python script_name.py` (replace `script_name` with the actual filename).
5. Follow the prompts to input the gun type, skin name, and condition of the CS:GO item.
6. Input the Skinport price in CAD.
7. Review the detailed pricing breakdown displayed.

## Functions:

- **get_steam_market_price(app_id, market_hash_name)**: Fetches the price of a CS:GO item from Steam Market.
- **convert_to_lira(cad_price, exchange_rate)**: Converts a price in CAD to Lira.
- **convert_to_cad(usd_price)**: Converts a price in USD to CAD.
- **display_price_info(market_hash_name, price_data, exchange_rate, skinport_price_cad)**: Displays a comprehensive breakdown of prices.

## Limitations:

- The conversion rates used in the script are hardcoded and may need updates over time to reflect current exchange rates.
- The Steam API might rate limit frequent requests, so be mindful of running the script multiple times in quick succession.

## Contribute:

If you would like to contribute, report bugs, or suggest improvements, feel free to make pull requests or open issues on the repository page.

## Disclaimer:

This tool is meant for informational purposes only. The exchange rates and conversion calculations might not be up-to-date. Always double-check any financial decisions.
