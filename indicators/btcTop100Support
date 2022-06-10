import matplotlib.pyplot as plt
import pandas as pd


# Функция для избавления от отрицательных занчений
def isNull(x):
    if x < 0:
        x = 0
    return x


# Получение данных
priceBtc = pd.read_csv(
    'https://api.blockchain.info/charts/market-price?timespan=all&sampled=false&metadata=true&cors=true&format=csv',
    names=['Price'])
transactionsWithoutRich = pd.read_csv(
    'https://api.blockchain.info/charts/n-transactions-excluding-popular?timespan=all&sampled=false&metadata=true'
    '&cors=true&format=csv', names=['Time', 'Value'])
transactions = pd.read_csv(
    'https://api.blockchain.info/charts/n-transactions?timespan=all&sampled=false&metadata=true&cors=true&format=csv',
    names=['Time', 'Value'])

# Создаем новый столбец с датой и временем
df = pd.DataFrame(priceBtc.index)
df.rename(columns={0: 'Time'}, inplace=True)

# Создаем столбец с ценой
df['Price'] = list(priceBtc['Price'])

# Создаем столбец с транзакциями топ 100 кошельками
df['tr100'] = (transactions['Value'] - transactionsWithoutRich['Value']).apply(isNull)

# Сумма транзакций за всe дни в день
df['SumTR'] = df['tr100'].cumsum()

# Среднее колличество транзакци
df['RichSupport'] = (df['Price'] * df['SumTR']).cumsum() / df['SumTR'].cumsum()

# Индекс меняем на время
df.index = df['Time']

# Строим график
df.plot(y=['Price', 'RichSupport'],
        color=['white', 'orange'], lw=0.7)
ax = plt.gca()
ax.set_facecolor('black')
plt.yscale('log')
plt.show()
