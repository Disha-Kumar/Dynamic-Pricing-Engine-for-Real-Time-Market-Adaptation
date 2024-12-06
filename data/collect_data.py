import requests
from bs4 import BeautifulSoup

def get_competitor_prices():
    url = 'https://zylalabs.com/api-marketplace/data/prices+comparison+api/2332'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        prices = [item['price'] for item in data['items']]
        return prices
    except requests.exceptions.RequestException as e:
        print(f"HTTP error occurred: {e}")
        return []
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return []

def get_inventory_levels():
    url = 'https://developer.zettle.com/docs/api/inventory/overview'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        inventory_levels = [item['inventory_level'] for item in data['items']]
        return inventory_levels
    except requests.exceptions.RequestException as e:
        print(f"HTTP error occurred: {e}")
        return []
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return []

# Example usage
competitor_prices = get_competitor_prices()
inventory_levels = get_inventory_levels()
