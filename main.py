from brands.bb_main import get_bb_price
from brands.grown_main import get_grown_price
from brands.keyzar_main import get_keyzar_price
from services.sheets.sheets import SheetHelper
from utils.time import assign_date


sheet = SheetHelper("Sheet1")
[date_curr_row, date_curr_col,current_date ,current_time] =  assign_date(sheet)

bb_curr_cell = {"row": date_curr_row,"col": 3}
keyzar_curr_cell = {"row": date_curr_row,"col": 6}
grown_curr_cell = {"row": date_curr_row,"col": 9}


bb_price =  get_bb_price()
sheet.update_cell(bb_curr_cell["row"], bb_curr_cell["col"],bb_price)

keyzar_price = get_keyzar_price()
sheet.update_cell(keyzar_curr_cell["row"], keyzar_curr_cell["col"],keyzar_price)

grown_price = get_grown_price()
sheet.update_cell(grown_curr_cell["row"], grown_curr_cell["col"],grown_price)

