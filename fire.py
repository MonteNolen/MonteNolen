import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'MODIS_C6_1_Global_24h.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #row_count = sum(1 for row in f) # подсчет количества строк (одна строка - 1 очаг возгорания)

    lats, lons, brightness = [], [], []
    for row in reader:
        lats.append(row[0])
        lons.append(row[1])
        brightness.append(float(row[2]))
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [0.1*bright//2 for bright in brightness],
        'color': brightness,
        'colorscale': 'Blackbody',
        'reversescale': True,
        'colorbar': {'title': 'Fire brightness'},
    },
}]
my_layout = Layout(title="Карта лесных пожаров по всему миру")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_firemap.html')
