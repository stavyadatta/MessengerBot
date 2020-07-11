import requests, json
import pandas as pd
import plotly.express as px
import numpy as np

countries=dict()
url = "https://api.covid19api.com/countries"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
json_data = response.json()

for i in json_data:
    countries[i['Country']]=i['Slug']

country=input('Enter the name of the country:')
cases_type=input('Enter the case type(confirmed, deaths or recovered):')
for i in countries:
    if i==country:
        country_slug=countries[i]
        

url = "https://api.covid19api.com/dayone/country/"+country_slug+"/status/"+cases_type

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
json_data = response.json()
l=list()
for i in json_data:
    l.append(i['Cases'])


if cases_type=='recovered':
    s='recoveries'
elif cases_type=='confirmed':
    s='confirmed cases'
elif cases_type=='deaths':
    s='deaths'
    

x=np.arange(len(l))
df = pd.DataFrame({'Days passed':x,'COVID '+s.capitalize():l})
fig = px.line(df, x="Days passed", y='COVID '+s.capitalize())
fig.update_traces(mode="markers+lines")
fig.update_xaxes(ticks="inside")
fig.update_layout(title="COVID STATISTICS", xaxis_title="Number of days", yaxis_title="Number of COVID "+s+" in "+country)
fig.show()

