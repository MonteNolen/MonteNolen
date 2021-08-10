import csv
import plotly.graph_objects as go
from plotly.graph_objs import Bar, Layout
from plotly import offline
from datetime import datetime

from matplotlib import pyplot as plt

# перевод фаренгейтов в цельсий
def fah2cel(fah):
    cel = 5.0*(fah - 32) / 9
    return float("%.1f" % cel)

filename = '2678048.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Чтение максимальных температур
    highs, lows, dates, temp = [], [], [], []
    for row in reader:
        try:
            high = fah2cel(int(row[4])) # перевод фаренгейтов в цельсий
            low = fah2cel(int(row[5]))
        except ValueError: #проверка на пустые строки и не int
            pass
        else:
            name = row[1]
            date = datetime.strptime(row[2], "%Y-%m-%d").date() # добавление даты без времени
            if 'SITKA AIRPORT, AK US' in name:
                highs.append(high)
                lows.append(low)
                dates.append(date)
                #temp.append(high)
                #temp.append(low)
        highs, lows, dates = highs[:50], lows[:50], dates[:50]
# Нанесение данных на диаграмму.
#x_value = list(range(1, len(temp)))
#data = [Bar(x=(x_value, dates), y=temp)]
#x_axis_config = {'title': 'Дни', 'dtick': 1}
#y_axis_config = {'title': 'Наивысшая температура'}
#my_layout = Layout(title='Температура в городе Ситка, Аляска',
                    #xaxis=x_axis_config, yaxis=y_axis_config)
#offline.plot({'data': data, 'layout': my_layout}, filename='temp.html')

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
fig.autofmt_xdate()
plt.title("Sitka")
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

