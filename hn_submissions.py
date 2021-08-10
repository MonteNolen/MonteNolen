from operator import itemgetter
import requests
from plotly.graph_objects import Bar
from plotly import offline

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

#print(f"Status code: {r.status_code}")
# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Создание отдельного вызова API для каждой статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    #print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Построение словаря для каждой статьи.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        continue
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
reverse=True)
#выборка для графика по комментариям и ссылкам на статьи, с их названиями
titles, links, comm = [], [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title']) 
    news_name = submission_dict['title']
    news_url = submission_dict['hn_link']
    news_link = f"<a href='{news_url}'>{news_name}</a>"
    links.append(news_link)
    comm.append(submission_dict['comments'])

data = [{
    'type': 'bar',
    'x': links, 
    'y': comm,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
        'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news.html')