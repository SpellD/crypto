import matplotlib.pyplot as plt
import pandas as pd

# Для снятия ограничений при выводе в консоль
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Функция для избавления от отрицательных занчений
def isNull(x):
    a = 0
    if x < 0:
        a = 0
    else:
        a = x
    return (a)

# Получение данных
priceBtc = pd.read_csv('https://api.blockchain.info/charts/market-price?timespan=all&sampled=false&metadata=false&cors=true&format=csv', delimiter=',', names=['Time', 'Price'])
transactionsWithoutRich = pd.read_csv('https://api.blockchain.info/charts/n-transactions-excluding-popular?timespan=all&sampled=false&metadata=false&cors=true&format=csv',delimiter=',', names=['Time', 'Value'])
transactions = pd.read_csv('https://api.blockchain.info/charts/n-transactions?timespan=all&sampled=false&metadata=false&cors=true&format=csv', delimiter=',', names=['Time', 'Value'])

# Транзакции 100 самых богатых кошельков
transactions['Value'] = transactions['Value'] - transactionsWithoutRich['Value']
transactions['Value'] = transactions['Value'].apply(isNull)

# Индикатор средней стоимости биткоина умноженный на 35
y = []
n = 0
days = 1
for i in priceBtc['Price']:
    averagePrice = (i + n) / days * 35
    n += i
    days += 1
    y.append(averagePrice)

priceBtc['TopAverage'] = pd.Series(y)

# Сумма транзакций за все дни в день
sumTransactions = []
n2 = 0
for i in transactions['Value']:
    result = i + n2
    n2 += i
    sumTransactions.append(result)

transactions['SumTR'] = pd.Series(sumTransactions)

# Непонятная херня но когда-нибудь она пригодится
# td = []
# d = 1
# for i in transactions['SumTR']:
#     result = i / d
#     d += 1
#     td.append(result)
#
# transactions['hui'] = pd.Series(td)

# Цена в день умноженная на транзакции в день
priceBtc['PV'] = priceBtc['Price'] * transactions['Value']

# Сумма PV за все дни в день
sumPV = []
n3 = 0
for i in priceBtc['PV']:
    result = i + n3
    n3 += i
    sumPV.append(result)

priceBtc['SumPV'] = pd.Series(sumPV)

# Индикатор поддержки 100 богатейшими кошельками
priceBtc['RichSupport'] = priceBtc['SumPV'] / transactions['SumTR']

# Вывод последних значений
print('Average price for transactions', (priceBtc['Price'] * transactions['Value']).sum() / transactions['Value'].sum())
print('Top average price', priceBtc['TopAverage'].iloc[-1])
print('Price', priceBtc['Price'].iloc[-1])

# Вывод графиков
priceBtc.plot(x='Time', y=['Price', 'TopAverage', 'RichSupport'], color=['white' ,'#FF8373', '#FFD473'], lw=0.7, style=['-' ,'--', '-'])
ax = plt.gca()
ax.set_facecolor('black')
plt.yscale('log')
plt.show()