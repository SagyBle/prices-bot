import os
import gspread
from google.oauth2.service_account import Credentials

class SheetHelper:
    def __init__(self, sheet_name: str):
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        sheet_id = "1AkV0fknHWVy1DtIyA1UjZUVhrVGahSblZQfUu3EXZDo"

        # Dynamically resolve the path to credentials.json
        current_dir = os.path.dirname(os.path.abspath(__file__))
        credentials_path = os.path.join(current_dir, "credentials.json")

        creds = Credentials.from_service_account_file(credentials_path, scopes=scopes)
        client = gspread.authorize(creds)

        workbook = client.open_by_key(sheet_id)
        self.sheet = workbook.worksheet(sheet_name)

    def get_absolute_next_free_cell_by_column(self, row: int, col: int) -> tuple[int, int]:
        values = self.sheet.col_values(col)[row - 1:]
        offset = len(values)
        return row + offset, col

    def get_next_free_cell_by_column(self, row: int, col: int, max_rows: int = 100) -> tuple[int, int]:
        col_letter = gspread.utils.rowcol_to_a1(1, col)[0]
        cell_range = f"{col_letter}{row}:{col_letter}{row + max_rows - 1}"
        cells = self.sheet.get(cell_range)

        for idx, row_values in enumerate(cells):
            value = row_values[0] if row_values else ""
            if value.strip() == "":
                return row + idx, col

        return row + len(cells), col

    def update_cell(self, row: int, col: int, value: str):
        self.sheet.update_cell(row, col, value)

    def update_cell_a1(self, label: str, value: str):
        self.sheet.update_acell(label, value)

    def get_cell_value(self, row: int, col: int) -> str:
        return self.sheet.cell(row, col).value

    def update_row(self, row: int, values: list[str]):
        self.sheet.update(f"{row}:{row}", [values])