import json
from openpyxl import load_workbook

filename = "ticker_sector.json"

with open(filename, 'r') as file:
    data = json.load(file)

wb = load_workbook('WIW Data.xlsx')
sheet = wb.active
column = 'A'
values = [cell.value for cell in sheet[column]]

print(values)

