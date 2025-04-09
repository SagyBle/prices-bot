from bs4 import BeautifulSoup
import requests


def get_bb_bundle_price(url: str):
    try:
        result = requests.get(url)
        result.raise_for_status()  # Raises an error if the request fails

        doc = BeautifulSoup(result.text, "html.parser")

        # Find the <sale-price> element
        sale_price_tag = doc.find('sale-price', class_='text-lg text-on-sale')

        if sale_price_tag:
            sale_price = sale_price_tag.get_text(strip=True)
            return sale_price
        else:
            return None

    except Exception as e:
        print(f"Error fetching price: {e}")
        return None


# 🔍 Example usage
url = "https://bestbrilliance.com/products/lucy-lab-grown-diamond-ring-3-5-carat-14k-white-gold?variant=40982004564035"
bb_a_price = get_bb_bundle_price(url)

if bb_a_price:
    print(f"BB price: {bb_a_price}")
else:
    print("Sale price not found")


