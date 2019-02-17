import plotly.plotly as py
import plotly.figure_factory as ff
import csv
import random
import numpy as np
import pandas as pd


df_sample = pd.read_csv('DataMaps.csv')

df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']

colorscale = ["#FF0000","#FFFF00","#FFFF00","#7FFF00","#00FF00"]
endpts = list(np.linspace(1, 5, len(colorscale) - 1))
fips = df_sample['FIPS'].tolist()
values = df_sample['Sentiment Analysis'].tolist()

fig = ff.create_choropleth(
    fips=fips, values=values,
    binning_endpoints=endpts,
    colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='Sentiment on Bill X %',
    legend_title='% Sentiment (0-1s)'
)
py.iplot(fig, filename='Sentiment_Map')
