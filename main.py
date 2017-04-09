
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


htmlMonth = urlopen("https://www.eia.gov/dnav/ng/hist/rngwhhdM.htm")
htmlDay = urlopen("https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm")

mObj = BeautifulSoup(htmlMonth, 'lxml')
dObj = BeautifulSoup(htmlDay, 'lxml')

dataPriceMonth = []
dataDateMonth =[]
dataMonth =[]

dataPriceDay = []
dataDateDay = []
dataDay = []
repNone = ['N/A']
# getting monthly data

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
with open('monthly.csv', 'w', newline='') as fMonth:
    writer = csv.writer(fMonth, delimiter=',')
    writer.writerow(['Date', 'Price'])
    writer.writerows(dataMonth)


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

with open('daily.csv', 'w', newline='') as fDay:
    writer = csv.writer(fDay, delimiter=',')
    writer.writerow(['Date', 'Price'])
    writer.writerows(dataDay)
