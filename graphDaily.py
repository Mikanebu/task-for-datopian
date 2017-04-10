import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

#import data from csv
df = pd.read_csv('daily.csv')
df.head()

trace = go.Scatter(
                  x = df['Date'], y = df['Price'],
                  name='Dollars per Million Btu'
                  )
layout = go.Layout(
                  title='Henry Hub Natural Gas Spot Price (1997-2017)',
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True
                  )
fig = go.Figure(data=[trace], layout=layout)
# save as daily.png
py.image.save_as(fig, filename='daily.png')
# opens in Embed URL
py.plot(fig, filename='natural-gas-prices-daily')
