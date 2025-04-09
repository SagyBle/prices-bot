from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def getKeyzarStoneProductPrice(url: str) -> str | None:
    service = Service(executable_path="../chromedriver")
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)

        # click the "Oval" button
        oval_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Oval']]"))
        )
        oval_button.click()

        # click the "VVS2" button
        vvs2_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='VVS2']]"))
        )
        vvs2_button.click()

        # Step 3: Click the "E" color grade button
        e_color_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='E']]"))
        )
        e_color_button.click()

        # Step 5: Get first 5 diamond prices
        diamond_cards = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "CenterStoneProductCard"))
        )

        # ✅ Wait 2 seconds before collecting prices
        time.sleep(2)

        diamond_prices = []

        # Locate all stone card elements
        stone_divs = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "CenterStoneProductCard"))
        )

        print(f"💎 Found {len(stone_divs)} stones – printing first 5 only:")

        for i, card in enumerate(stone_divs[:5]):
            try:
                # Look for all elements with that class inside this card
                possible_prices = card.find_elements(By.CLASS_NAME, "text-customGray-500")

                # Filter for the one that has a dollar sign
                price_element = next((el for el in possible_prices if "$" in el.text), None)

                if price_element:
                    price = price_element.text.strip()
                    print(f"💎 Stone #{i + 1} price: {price}")
                else:
                    print(f"⚠️ Stone #{i + 1} – no price found")

            except Exception as e:
                print(f"❌ Error on stone #{i + 1}: {e}")




    except Exception as e:
        print("❌ Could not find the price div:", e)
        return None

    finally:
        driver.quit()


url = "https://keyzarjewelry.com/collections/center-stones?stoneType=labDiamond&configurationType=ring"
getKeyzarStoneProductPrice(url)