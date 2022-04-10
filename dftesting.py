import pandas as pd
df1 = pd.read_csv('stocks.csv')
#print(df1.index)
#print(df1)
#print(df1.groupby('Symbol'))
ser = df1.groupby(['Symbol', 'Date']).Close.mean()

#print(ser.index)
#print(ser.unstack())
print(ser.loc['AAPL'])
