from services.selenium.grown_selenium import get_grown_bundle_price

def get_grown_price():
    url = "https://www.grownbrilliance.com/2-1-2-ctw-oval-lab-grown-diamond-station-engagement-ring-platinum/pid/RIG1860X3-O200SO-LW?category_id=78"
    return get_grown_bundle_price(url)