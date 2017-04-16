import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

dataPriceDay = []
dataDateDay = []
dataDay = []
repNone = ['N/A']

htmlDay = urlopen("https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm")

dObj = BeautifulSoup(htmlDay, 'lxml')

def csv_daily():
    # getting daily data
    tableDataDay = dObj.find_all('td', {'class':'B6'})
    for dt3 in tableDataDay:
        dt3 = dt3.contents
        dataDateDay.append(dt3)
        #print(dataDateDay)
    tableDataDay = dObj.find_all('td', {'class':'B3'})
    for dt4 in tableDataDay:
        if len(dt4.contents) == 0:
            dataPriceDay.append(repNone)
        else:
            dt4 = dt4.contents
            dataPriceDay.append(dt4)
    for i in range(len(dataPriceDay)):
        if dataPriceDay[i] == ['N/A']:
            if i>0:
                #print(dataPriceDay[i-1])
                dataPriceDay[i] = dataPriceDay[i-1]
            else:
                dataPriceDay[i] = dataPriceDay[i+1]
    for x in range(0,len(dataPriceDay),5):
        for i in range(0,5):
            index = int(x/5)
            mydate =dataDateDay[index][0].strip()
            temp = mydate[0:4] + '/' + mydate[5:8] + '/' + mydate[9:11]
            mydate = datetime.strptime(temp, '%Y/%b/%d')
            mydate += timedelta(days=i)
            mydate = datetime.strftime(mydate, '%Y-%m-%d')
            dataDay.append([mydate, dataPriceDay[x+i][0]])

    with open('data/daily.csv', 'w', newline='') as fDay:
        writer = csv.writer(fDay, delimiter=',')
        writer.writerow(['Date', 'Price'])
        writer.writerows(dataDay)
