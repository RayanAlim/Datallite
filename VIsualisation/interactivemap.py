import pandas as pd
import geopandas as gdp
import plotly
import json

import plotly.express as px

df = pd.read_csv('/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/schools-in-nigeria/Schools-with-lat-long.csv')
df_wb = pd.read_csv("/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/world-bank-data/cons_agg_wave3_visit2.csv")
dff = gdp.read_file("/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/nigeria_geojson.geojson")
df_json = pd.read_json('/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/gistfile1.json')
geo_df_cities = gdp.read_file("/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/nigeria_lga_boundaries.geojson")
geo_df_states = gdp.read_file('/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/nigeria_state_boundaries.geojson')

fig = px.choropleth_mapbox(df, geojson=geo_df_cities.geometry, locations=geo_df_cities.index, color= geo_df_cities['admin0Pcod'],
                           mapbox_style="carto-positron",
                           center= {"lat":9.061068, 'lon':7.377189},
                           zoom=6
                          )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()