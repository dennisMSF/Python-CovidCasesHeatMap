from scipy.interpolate import interp1d
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_excel(r"Directroy where the data is")
list1 = df.cases.values.tolist()
m = interp1d([1,max(list1)],[5,16])
circle_radius = m(list1)
typelist = ['open-street-map','white-bg','carto-positron','carto-darkmatter', 'stamen-terrain','stamen-toner', 'stamen-watercolor']
for i in typelist:
	print(i)
	fig = px.density_mapbox(df,lat='Lat',lon='Long',radius = circle_radius,zoom=0,mapbox_style = i)
	fig.show()
