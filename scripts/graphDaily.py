import plotly.plotly as py
import plotly.graph_objs as go
import csv

date = []
price = []
counter = 0
csv_reader = csv.reader(open('../data/daily.csv'))
for row in csv_reader:
    if counter == 0:
        counter += 1
        continue
    date.append(row[0])
    price.append(row[1])
trace = dict(x = date, y = price)
data = [trace]
# save as daily.png
py.image.save_as(data, filename='../data/daily.png')
# opens in Embed URL
py.plot(data, filename='natural-gas-prices-daily')
