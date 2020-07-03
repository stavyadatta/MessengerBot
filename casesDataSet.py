import requests, json
import modifyingMessages
import traceback

def numberOfCasesInCountry(Country):
    url_summary = "https://api.covid19api.com/summary"

    payload = {}
    headers = {}

    response = requests.request("GET", url_summary, headers=headers, data=payload)
    json_data_summary = response.json()

    cindex = binary_search_countries(json_data_summary['Countries'], Country)
    try:
        return changeJson('TotalConfirmed', json_data_summary, cindex), \
               changeJson('TotalDeaths', json_data_summary, cindex), \
               changeJson('TotalRecovered', json_data_summary, cindex), \
               changeJson('NewConfirmed', json_data_summary, cindex), \
               changeJson('NewRecovered', json_data_summary, cindex), \
               changeJson('NewDeaths', json_data_summary, cindex)

    except TypeError:
        traceback.print_exc()
        return modifyingMessages.alternate_text


def changeJson(parameter, json_data_summary, cindex):
    return "{:,}".format(json_data_summary['Countries'][cindex][parameter])


# Geeksforgeeks - https://www.geeksforgeeks.org/python-program-for-binary-search/
def binary_search_countries(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    i = 0
    while low <= high:
        i = i + 1
        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid]['Country'] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid]['Country'] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

    return ''
