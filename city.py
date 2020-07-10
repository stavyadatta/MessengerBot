import json
from mergeSort import Sort_Tuple

with open('hospitalData.json', 'r') as fp:
    data = json.load(fp)
city_list = []
for state in data.keys():
    for city in data[state]:
        city_list.append((city, state))
city_list = Sort_Tuple(city_list)
print(len(city_list))


