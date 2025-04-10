from bs4 import BeautifulSoup
import requests
import re


def get_bb_bundle_price(url: str):
    try:
        result = requests.get(url)
        result.raise_for_status()  # Raises an error if the request fails

        doc = BeautifulSoup(result.text, "html.parser")

        # Find the <sale-price> element
        sale_price_tag = doc.find('sale-price', class_='text-lg text-on-sale')

        if sale_price_tag:
            sale_price_text = sale_price_tag.get_text(strip=True)
            number_str = re.sub(r"[^\d.]", "", sale_price_text.replace(",", ""))
            price = float(number_str)
            return price
        else:
            return None

    except Exception as e:
        return None



