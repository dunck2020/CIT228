import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore data structure
filename = 'Chapter16/recent_seven_days_quakes.json'
with open(filename, encoding="utf8") as f:
    all_eq_data = json.load(f)
    
all_eq_data = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the quakes
data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'color' : mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : 
        {
            'title': 'Magnitude'
        }
    }
}]
my_layout = Layout(title='Global Earthquakes Last 7 days')
fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='Chapter16/global_quakes_last7days.html')
