import csv

import pandas as pd

import plotly_express as px

df1 = pd.read_csv("filter_data.csv")

solar_chart_mass_graph = px.bar(x = df1["star_names"], y = df1["mass"])
solar_chart_mass_graph.show()

solar_chart_radius_graph = px.bar(x = df1["star_names"], y = df1["radius"])
solar_chart_radius_graph.show()

solar_chart_gravity_graph = px.bar(x = df1["star_names"], y = df1["gravity"])
solar_chart_gravity_graph.show()

solar_chart_distance_graph = px.bar(x = df1["star_names"], y = df1["distance"])
solar_chart_distance_graph.show()