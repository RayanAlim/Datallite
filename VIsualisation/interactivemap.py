import pandas as pd
import geopandas as gdp
import plotly
import json

import plotly.express as px

df = pd.read_csv('/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/Schools-with-lat-long.csv')
df_wb = pd.read_csv("/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/world-bank-data/cons_agg_wave3_visit2.csv")
dff = gdp.read_file("/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/nigeria_geojson.geojson")
geo_df = gdp.read_file("/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/nigeria_geojson.geojson")

fig = px.choropleth_mapbox(df, geojson=geo_df.geometry, locations='geometry', color='lga',
                           mapbox_style="carto-positron",
                           zoom=4
                          )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()