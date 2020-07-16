import requests, json
import traceback
from binary_search import binary_search


def numberOfCasesInCountry(Country):
    url_summary = "https://api.covid19api.com/summary"

    payload = {}
    headers = {}

    response = requests.request("GET", url_summary, headers=headers, data=payload)
    json_data_summary = response.json()

    cindex = binary_search(json_data_summary['Countries'], Country, 'Country')
    try:
        return changeJson('TotalConfirmed', json_data_summary, cindex), \
               changeJson('TotalDeaths', json_data_summary, cindex), \
               changeJson('TotalRecovered', json_data_summary, cindex), \
               changeJson('NewConfirmed', json_data_summary, cindex), \
               changeJson('NewRecovered', json_data_summary, cindex), \
               changeJson('NewDeaths', json_data_summary, cindex)

    except TypeError:
        traceback.print_exc()
        return 'blhjk'


def changeJson(parameter, json_data_summary, cindex):
    return "{:,}".format(json_data_summary['Countries'][cindex][parameter])


