import pandas as pd
import plotly
import json


df = pd.read_csv("/Users/alim/Documents/GitHub/Team-4-AI-4-Good-lab/datasets/schools-in-nigeria/raw-files/raw-csv-files/Religious-schools.csv",
                   dtype={"fips": str})
                   
dff = gdp.read_file("private-schools.geojson")

import plotly.express as px

fig = px.choropleth(df, geojson=dff, locations='geometry', color='no_of_students',
                           color_continuous_scale="no_of_teachers",
                           range_color=(0, 12),
                           scope="africa"
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()