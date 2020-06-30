import pandas as pd
import requests, json
import datetime


def return_news(country):
    page = pd.read_html('https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes')
    countries = dict()
    df = page[0]
    for i in range(len(df)):
        countries[str(df.iloc[:, 0][i])] = str(df.iloc[:, 3][i])

    Previous_Date = datetime.datetime.today() - datetime.timedelta(days=15)
    dt = str(Previous_Date)[:10]
    url_practice = "https://newsapi.org/v2/top-headlines?q=COVID&from=" + dt + "&sortBy=popularity&apiKey=565324e8912a47cdbce2d37b8639d5ed&pageSize=100&page=1&country=" + \
                   countries[country]

    payload = {}
    headers = {}

    response = requests.request("GET", url_practice, headers=headers, data=payload)
    json_data = response.json()
    answer = list()
    for i in range(len(json_data['articles'])):
        answer.append([json_data['articles'][i]['source']['name'], json_data['articles'][i]['title'],
                       json_data['articles'][i]['url']])
    return answer


news = return_news('India')  # Country name goes here
print(news)
