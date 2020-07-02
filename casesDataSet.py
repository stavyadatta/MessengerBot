import requests, json


def numberOfCasesInCountry(Country):
    url = "https://api.covid19api.com/countries"
    country_list = list()
    slug_list = list()
    payload = {}
    headers = {}
    #
    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = response.json()
    for i in range(len(json_data)):
        country_list.append(json_data[i]['Country'])
        slug_list.append(json_data[i]['Slug'])
        print(response)

    for i in range(len(country_list)):
        if Country == country_list[i]:
            country_index = i
            break
    slug_country = slug_list[country_index]

    url_summary = "https://api.covid19api.com/summary"

    payload = {}
    headers = {}

    response = requests.request("GET", url_summary, headers=headers, data=payload)
    json_data_summary = response.json()

    cindex = ''
    for i in range(len(json_data_summary['Countries'])):
        if (json_data_summary['Countries'][i]['Country'] == Country):
            cindex = i
            break

    #print("Total confirmed cases in total:" + str(json_data_summary['Countries'][cindex]['TotalConfirmed']))
    try:
        return str(json_data_summary['Countries'][cindex]['TotalConfirmed']), \
               str(json_data_summary['Countries'][cindex]['TotalDeaths'])
    except TypeError:
        return 'Didnt get what you are saying'
    # print("Total deaths in total:" + str(json_data_summary['Countries'][cindex]['TotalDeaths']))
