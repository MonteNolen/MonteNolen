import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#открываем и читаем
filename = '1.0_month.json'
with open(filename) as f:
    all_data = json.load(f)
#форматируем для удобства
readable_file = 'format.json'
with open(readable_file, 'w') as f:
    json.dump(all_data, f, indent=4)

#выбираем все по ключу features
all_dicts = all_data["features"]
#достаем название графика
layout_title = all_data["metadata"]["title"]
mags, lons, lats, hover_texts= [], [], [], []
for dicts in all_dicts:
    mags.append(dicts["properties"]["mag"])
    lons.append(dicts["geometry"]["coordinates"][0])
    lats.append(dicts["geometry"]["coordinates"][1])
    hover_texts.append(dicts["properties"]["title"])
# Нанесение данных на карту.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [4*mag for mag in mags],
        'color': mags,
        'colorscale': 'Cividis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
#
my_layout = Layout(title=layout_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
