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

print(state_wise_numbers('Delhi'))