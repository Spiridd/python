# find the crime that was done most times in 2015
import csv
import datetime


with open('Crimes.csv', 'rt') as f:
    reader = csv.reader(f)
    labels = next(reader)
    date_index = labels.index('Date')
    primary_type_index = labels.index('Primary Type')
    crimes = {}
    for row in reader:
        year = datetime.datetime.strptime(row[date_index], '%m/%d/%Y %H:%M:%S %p').year
        if year == 2015:
            primary_type = row[primary_type_index]
            try:
                crimes[primary_type] += 1
            except KeyError:
                crimes[primary_type] = 1
    # find max
    crimes = list(crimes.items())
    crimes.sort(key=lambda x: x[1], reverse=True)
    print(crimes[0])
