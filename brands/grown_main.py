from services.selenium.grown_selenium import get_grown_bundle_price


def get_grown_price():
    print("🔍 Fetching Grown Brilliance price...")

    url = "https://www.grownbrilliance.com/2-1-2-ctw-oval-lab-grown-diamond-station-engagement-ring-platinum/pid/RIG1860X3-O200SO-LW?category_id=78"
    price = get_grown_bundle_price(url)

    if price is not None:
        print(f"💰 Grown Brilliance price: ${price:.2f}")
    else:
        print("⚠️ Failed to fetch Grown Brilliance price.")

    return price