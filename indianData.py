import requests, json
from binary_search import binary_search
import state_list


def state_wise_numbers(text):
    url = "https://api.rootnet.in/covid19-in/stats/latest"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    json_data_summary = response.json()
    state_wise_count = list(json_data_summary['data']['regional'])
    state = binary_search(state_wise_count, text, 'loc')
    return state_wise_count[state]


def beds_state_wise(text):
    with open('hospitalData.json', 'r') as fp:
        data = json.load(fp)
    state_hospitals = data[text]
    list_of_hospitals = []
    for city in state_hospitals.keys():
        for hospital in state_hospitals[city]:
            list_of_hospitals.append(hospital)
    return list_of_hospitals

test = beds_state_wise('Maharastra')
print(test)