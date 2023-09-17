# Steam Arbitrage Profit Calculator

This program helps users to determine the potential profit from arbitrage opportunities between the Steam market and Skinport for CS:GO skins.

![image](https://github.com/joshuabastien/SteamArbitrageProfitCalc/assets/77856927/5ea0ea74-bde1-4beb-9368-5a2ed63a8f36)
![image](https://github.com/joshuabastien/SteamArbitrageProfitCalc/assets/77856927/6dfbc2a4-5d28-49c6-a80d-e2cc01766a60)

(The 'Difference' is the profit of that item and the 'Ratio' is the ROI of buying that item.)

## Features

1. **Web Scraping**: The program can scrape skin details from a given URL using the `BeautifulSoup` library. It fetches details like the item link, price, title, name, and description.
   
   [View Code](https://github.com/joshuabastien/SteamArbitrageProfitCalc/blob/main/scrape-webpage.py)

2. **Steam Market Price Checker**: The program can fetch the price of a CS:GO skin from the Steam market in both Canadian Dollars (CAD) and Turkish Lira. It provides details like the lowest and median price, adjusted price, ratio, and difference in price compared to Skinport.
   
   [View Code](https://github.com/joshuabastien/SteamArbitrageProfitCalc/blob/main/getskinpricesteam.py)

3. **GUI**: The program offers a graphical user interface built using `tkinter` where users can input details about the skin they want to check. The GUI provides options for specifying if the weapon is a StatTrak™ or a Knife/Glove, the weapon type, skin name, condition, and the Skinport price in CAD.

## Usage

1. Run the main program.
2. Use the GUI to input the details of the skin you want to check.
3. Click on the "Submit" button to get the price details.
