
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

dataPriceMonth = []
dataDateMonth =[]
dataMonth =[]
repNone = ['N/A']

htmlMonth = urlopen("https://www.eia.gov/dnav/ng/hist/rngwhhdM.htm")

mObj = BeautifulSoup(htmlMonth, 'lxml')
def csv_monthly():

    tableDataMonth = mObj.find_all('td', {'class':'B4'})
    for dt1 in tableDataMonth:
            dt1= dt1.contents
            dataDateMonth.append(dt1)
    tableDataMonth = mObj.find_all('td', {'class':'B3'})
    for dt2 in tableDataMonth:
        if len(dt2.contents) == 0:
            dataPriceMonth.append(repNone)
        else:
            dt2= dt2.contents
            dataPriceMonth.append(dt2)

    for y in range(0, len(dataPriceMonth), 12):
        for j in range(0,12):
            index1 = int(y/12)
            mydate = datetime(int(dataDateMonth[index1][0].strip()), j+1, 1)
            mydate = datetime.strftime(mydate, '%Y-%m-%d')
            dataMonth.append([mydate,dataPriceMonth[y+j][0]])

    # writing to monthly CSV file
    with open('data/monthly.csv', 'w', newline='') as fMonth:
        writer = csv.writer(fMonth, delimiter=',')
        writer.writerow(['Date', 'Price'])
        writer.writerows(dataMonth)
