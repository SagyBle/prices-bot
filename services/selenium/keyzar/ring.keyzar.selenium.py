from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def get_keyzar_ring_price(url: str) -> str | None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.abspath(os.path.join(current_dir, "..", "chromedriver"))

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)

        # Wait up to 15 seconds for the price div to load
        price_div = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tangiblee-price"))
        )

        if price_div:
            price = price_div.text.strip()
            print("💰 Price:", price)
            return price
        else:
            print("❌ Price div found but no text inside.")
            return None

    except Exception as e:
        print("❌ Could not find the price div:", e)
        return None

    finally:
        driver.quit()


url = "https://keyzarjewelry.com/products/the-ashley-setting-round-14k-white-gold-pave"
get_keyzar_ring_price(url)