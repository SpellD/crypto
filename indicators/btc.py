import matplotlib.pyplot as plt
import csv
import datetime
import requests
import os
import matplotlib.mlab as mlab

#Получаем инфу
price = requests.get('https://api.blockchain.info/charts/market-price?format=csv&sampled=false&timespan=all').text
mvrv = requests.get('https://api.blockchain.info/charts/mvrv?timespan=all&sampled=true&metadata=false&cors=true&format=csv').text

#Запись в файл данных MVRV
with open('mvrv.csv', 'a') as file:
    file.write(mvrv)

yMV = []
#запись в массив данных MVRV
with open('mvrv.csv', 'r') as sales_csv:
    plots = csv.reader(sales_csv, delimiter=',')
    for row in plots:
        yMV.append(row[1])

yMV = [float(i) for i in yMV]

#Запись в файл данных цена
with open('priceBTC.csv', 'a') as file:
    file.write(price)

x = []
y = []

#запись в массив данных цена
with open('priceBTC.csv', 'r') as sales_csv:
    plots = csv.reader(sales_csv, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

y = [float(i) for i in y]
x = [datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S') for i in x]

#realized price
rv = []

for i in y:
    for j in yMV:
        k = i / j
        rv.append(k)

fig = plt.figure()
fig.patch.set_facecolor('black')

ax = plt.axes()
ax.set_facecolor("black")

ax.spines['bottom'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['top'].set_color('white')

ax.xaxis.label.set_color('white')

ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

plt.plot(x, y, label='Loaded from file!', color="white",lw=0.7)
plt.xlabel('x')
plt.yscale('log')
plt.show()

# open('priceBTC.csv', 'w').close()

os.remove("priceBTC.csv")

os.remove("mvrv.csv")