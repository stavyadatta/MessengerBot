import pycountry, datetime, requests,json
country=input("Enter a country's name: ")
countryClass=pycountry.countries.get(name=country)
code=countryClass.alpha_2
Previous_Date = datetime.datetime.today() - datetime.timedelta(days=15) 
dt=str(Previous_Date)[:10]
 
url_practice="https://newsapi.org/v2/top-headlines?q=COVID&from="+dt+"&sortBy=popularity&apiKey=565324e8912a47cdbce2d37b8639d5ed&pageSize=100&page=1&country="+code

payload = {}
headers= {}

response = requests.request("GET", url_practice, headers=headers, data = payload)
json_data = response.json()

answer=list()
for i in range(len(json_data['articles'])):
    answer.append([json_data['articles'][i]['source']['name'],json_data['articles'][i]['title'],json_data['articles'][i]['url']])

print(answer)






