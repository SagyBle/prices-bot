from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import re



def get_grown_bundle_price(url: str) -> str | None:
    # Find chromedriver in the SAME folder as this file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.join(current_dir, "chromedriver")

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)

        # Wait up to 15 seconds for the price div to load
        price_div = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_our_price"))
        )

        if price_div and price_div.text:
            price_text = price_div.text.strip()
            clean_price = re.sub(r"[^\d.]", "", price_text)


            return float(clean_price) if clean_price else None
        else:
            return None

    except Exception as e:
        return None

    finally:
        driver.quit()

# url = "https://www.grownbrilliance.com/2-1-2-ctw-oval-lab-grown-diamond-station-engagement-ring-platinum/pid/RIG1860X3-O200SO-LW?category_id=78"
# print(get_grown_bundle_price(url))