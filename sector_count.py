import json
from openpyxl import load_workbook

filename = "ticker_sector.json"

with open(filename, 'r') as file:
    data = json.load(file)

wb = load_workbook('WIW Data.xlsx')
sheet = wb.active
column = 'A'
values = [cell.value for cell in sheet[column]]
positions = [cell.value for cell in sheet['B']]
#iterate the values list and print all of them

short_cnt = {}
long_cnt = {}
idx = 0
for value in values:
    if value in data:
        print(value, data[value])
        if(positions[idx]==1):
            if(not (data[value] in long_cnt)):
                long_cnt[data[value]] = 1
            else:
                long_cnt[data[value]] += 1
        else:
            if(not (data[value] in short_cnt)):
                short_cnt[data[value]] = 1
            else:
                short_cnt[data[value]] += 1
    else:
        continue
    idx += 1

print(short_cnt)
print(long_cnt)