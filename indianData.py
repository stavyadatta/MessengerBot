import requests, json
from binary_search import binary_search
import traceback


def state_wise_numbers(text):
    url = "https://api.rootnet.in/covid19-in/stats/latest"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    json_data_summary = response.json()
    state_wise_count = list(json_data_summary['data']['regional'])
    print(text + " the state tat came to state_wise number")
    state = binary_search(state_wise_count, text, 'loc')
    try:
        return state_wise_count[state]
    except TypeError:
        return False


def beds_state_wise(text):
    with open('hospitalData.json', 'r') as fp:
        data = json.load(fp)
    try:
        state_hospitals = data[text]
    except KeyError:
        traceback.print_exc()
        return False
    list_of_hospitals = []
    for city in state_hospitals.keys():
        for hospital in state_hospitals[city]:
            list_of_hospitals.append(hospital)
    return list_of_hospitals


def beds_city_wise(tuple):
    with open('hospitalData.json', 'r') as fp:
        data = json.load(fp)
    try:
        city_hospitals = data[tuple[1]][tuple[0]]
    except KeyError:
        traceback.print_exc()
        return False
    list_of_hospitals = []
    for hospital in city_hospitals:
        list_of_hospitals.append(hospital)
    return list_of_hospitals

#test = beds_state_wise('Maharastra')
#print(test)