from services.selenium.keyzar.stone_keyzar_selenium import get_keyzar_stone_price
from services.selenium.keyzar.ring_keyzar_selenium import get_keyzar_ring_price
from statistics import mean


def get_keyzar_price():
    print("🔍 Fetching Keyzar stone prices...")
    stone_url = "https://keyzarjewelry.com/collections/center-stones?stoneType=labDiamond&configurationType=ring"
    stones_prices = get_keyzar_stone_price(stone_url)
    print(f"💎 Found stone prices: {stones_prices}")

    stone_avg = mean(stones_prices)
    print(f"📊 Calculated stone average: ${stone_avg:.2f}")

    print("🔍 Fetching Keyzar ring price...")
    ring_url = "https://keyzarjewelry.com/products/the-ashley-setting-round-14k-white-gold-pave"
    ring_price = get_keyzar_ring_price(ring_url)
    print(f"💍 Ring price: ${ring_price:.2f}")

    total_price = stone_avg + ring_price
    print(f"💰Keyzar bundle price: ${total_price:2f}\n")

    return total_price