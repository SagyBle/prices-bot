
from datetime import datetime

def assign_date(sheet):
    now = datetime.now()
    current_date = now.date()
    current_time = now.time()
    [date_row, date_col] =  sheet.get_absolute_next_free_cell_by_column(3,1)

    sheet.update_cell(date_row,date_col, str(current_date))
    sheet.update_cell(date_row,date_col + 1, str(current_time))
    return [date_row, date_col,current_date ,current_time]