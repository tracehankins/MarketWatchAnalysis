import csv

ticker_sector = {}
with open("nasdaq_ticker_data.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    next(reader, None)  # skip the headers
    data_read = [row for row in reader]
    
    for row in data_read:
        ticker_sector[row[0]] = row[9]

#write the dictionary to a json file
import json
with open('ticker_sector.json', 'w') as fp:
    #format the json file so it looks ncie too
    json.dump(ticker_sector, fp, indent=4)