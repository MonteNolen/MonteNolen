import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'MODIS_C6_1_Global_24h.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    lats, lots, brightness = [], [], []
    for row in reader:
        lats.append(row[0])
        lots.append(row[1])
        brightness.append(row[2])
        