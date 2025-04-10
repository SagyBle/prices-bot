import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_keyzar_stone_price(url: str) -> list[float]:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.abspath(os.path.join(current_dir, "..", "chromedriver"))

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)

        # Click the "Oval" button
        oval_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Oval']]"))
        )
        oval_button.click()

        # Click the "VVS2" button
        vvs2_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='VVS2']]"))
        )
        vvs2_button.click()

        # Click the "E" color grade button
        e_color_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='E']]"))
        )
        e_color_button.click()

        # Wait for diamond cards to appear
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "CenterStoneProductCard"))
        )

        # Wait 2 seconds before collecting prices
        time.sleep(2)

        # Locate all stone card elements
        stone_divs = driver.find_elements(By.CLASS_NAME, "CenterStoneProductCard")

        diamond_prices = []

        for card in stone_divs[:5]:
            try:
                # Find all possible price elements
                possible_prices = card.find_elements(By.CLASS_NAME, "text-customGray-500")
                price_element = next((el for el in possible_prices if "$" in el.text), None)

                if price_element:
                    price_text = price_element.text.strip().replace("$", "").replace(",", "")
                    diamond_prices.append(float(price_text))
            except Exception as e:
                print(f"❌ Error while parsing price: {e}")

        return diamond_prices

    except Exception as e:
        print("❌ Could not collect prices:", e)
        return []

    finally:
        driver.quit()


# Example usage:
# url = "https://keyzarjewelry.com/collections/center-stones?stoneType=labDiamond&configurationType=ring"
# prices = get_keyzar_stone_price(url)
# print(prices)