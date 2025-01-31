""" 
This is a project I made following the Python Mega Course in Udemy, the purpose is to create an interactive map of whatever you want. 
In this case the map is about Volcanoes and where they are in the United States of America, each volcanoe has a pop up feature to see different information of it.
All the information in this case is stored in a txt file.
"""

import folium 
import pandas as pd

# Read the txt file
data = pd.read_csv('Volcanoes.txt')

# Get the latitude, longitude and elevation values
latitude = list(data['LAT'])
longitude = list(data['LON'])
elev = list(data['ELEV'])

# Define the icons colours depending on the elevation
def icon_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else: 
        return 'red'

# Create the map first location, this is where we will be located when he run the script and the map it's created
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles='OpenStreetMap')

# Create the Group Volcanoes
fgv = folium.FeatureGroup(name='Volcanoes')

# Create a Circle marker for each Volcanoe in the txt file based on the latitude and longitude
for lt, ln, el in zip(latitude, longitude, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(str(el) + ' m', parse_html=True), fill_color=icon_color(el)
                                     , color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Volcanoes.html')

