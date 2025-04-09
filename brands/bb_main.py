from services.bs.bb_bs import get_bb_bundle_price

def get_bb_price():
    url = "https://bestbrilliance.com/products/lucy-lab-grown-diamond-ring-3-5-carat-14k-white-gold?variant=40982004564035"
    return get_bb_bundle_price(url)