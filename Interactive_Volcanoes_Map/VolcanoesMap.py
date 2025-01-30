import folium 
import pandas as pd

data = pd.read_csv('Volcanoes.txt')

latitude = list(data['LAT'])
longitude = list(data['LON'])
elev = list(data['ELEV'])

def icon_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else: 
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles='OpenStreetMap')

fgv = folium.FeatureGroup(name='Volcanoes')

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

