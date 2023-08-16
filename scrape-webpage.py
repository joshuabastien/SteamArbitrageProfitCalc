import requests
from bs4 import BeautifulSoup

def fetch_all_skin_details(url):
    response = requests.get(url)
    items = []
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the containing <div> elements of the skins on the page
        all_skin_divs = soup.find_all('div', {'class': 'ItemPreview-commonInfo'})
        
        for skin_div in all_skin_divs:
            # Find the relevant <a> tag within the containing <div> of each skin
            link_tag = skin_div.find_parent('a', {'class': 'ItemPreview-link'})
            
            # Find the price <div> tag within the containing <div> of each skin
            price_tag = skin_div.find('div', {'class': 'Tooltip-link'})
            
            # Find the ItemPreview-itemTitle, ItemPreview-itemName and ItemPreview-itemText <div> tags within the containing <div> of each skin
            title_tag = skin_div.find('div', {'class': 'ItemPreview-itemTitle'})
            name_tag = skin_div.find_next('div', {'class': 'ItemPreview-itemName'})
            text_tag = skin_div.find_next('div', {'class': 'ItemPreview-itemText'})
            
            item_link = 'https://skinport.com' + link_tag['href'] if link_tag else 'Link not found'
            item_price = price_tag.text if price_tag else 'Price not found'
            item_title = title_tag.text if title_tag else 'Title not found'
            item_name = name_tag.text if name_tag else 'Name not found'
            item_text = text_tag.text if text_tag else 'Text not found'
            
            # Append item details to the items list
            items.append({
                'Item Link': item_link,
                'Item Price': item_price,
                'Item Title': item_title,
                'Item Name': item_name,
                'Item Text': item_text
            })
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    
    return items

def print_item_details(items):
    for index, item in enumerate(items, 1):
        print(f"Item {index}:")
        print(f"  Link: {item['Item Link']}")
        print(f"  Price: {item['Item Price']}")
        print(f"  Title: {item['Item Title']}")
        print(f"  Name: {item['Item Name']}")
        print(f"  Description: {item['Item Text']}")
        print("-" * 40)

# Example usage
url = 'https://skinport.com/market?cat=Rifle'
items = fetch_all_skin_details(url)
print_item_details(items)