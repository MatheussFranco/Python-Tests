import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

plt.style.use('fivethirtyeight')
pd.options.display.max_columns = 500
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]

from fredapi import Fred

fred_key = '23dd64824b0de886cf1a9c327103bec3'

# Create the fred object
fred = Fred(api_key=fred_key)

# Search for economic data 

# OBS: S&P (Standart & Poor's 500 Index) is a market-capitalization-weighted index
# of 500 leading publicly traded companies in the U.S.

fred.search('S&P')

sp_search = fred.search('S&P', order_by='popularity')
sp_search.head()


# print("\n\nShape of SP search", sp_search.shape)

# print("\n\n")
# df = pd.DataFrame(sp_search, columns=['id','title', 'notes'])
# select_cat = df.loc[df['id'] == 'SP500']

# print(select_cat)

# print("\n\n")
# col = 'notes'
# index = 0
# cell_val = select_cat.iloc[index][col]

# print("Notes about SP500: ", cell_val)



# Pull Raw Data and Plot
sp500 = fred.get_series(series_id='SP500')

plt.subplots()
sp500.plot(figsize=(10,5), title='S&P500 plot', lw=1)

# Pull and Join Multiple data series
unemp_results = fred.search('unemployement')
# print(unemp_results)

unrate = fred.get_series('UNRATE')

unemp_df = fred.search('unemployent rate state', filter=('frequency', 'Monthly'))

# filtrar linhas com a coluna seasonal_ajustment de valores Seasonally Adjusted
unemp_df = unemp_df.query('seasonal_adjustment == "Seasonally Adjusted" and units == "Percent"')
print(unemp_df)

plt.subplots()
unrate.plot(figsize=(10,5), title='Unemployement plot', lw=1)



plt.show()


