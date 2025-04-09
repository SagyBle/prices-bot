# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()
#
# @app.get("/test")
# def read_root():
#     bb_price =  get_bb_price()
#     grown_price = get_grown_price()
#     return {"message": "🚀 Hello from FastAPI!", "bb_price": bb_price, "grown_price": grown_price}

from brands.bb_main import get_bb_price
from brands.grown_main import get_grown_price


bb_price =  get_bb_price()
grown_price = get_grown_price()


print({bb_price, grown_price} )