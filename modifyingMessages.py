from binary_search import binary_search
from testingDataset import testing_data_country_wise
import casesDataSet
import HospitalLocation
import pycountry
import news
import state_list
import indianData


# when info is not found
alternate_text = "Didn't get your text, please try again later"


def textDecider(text):
    textReturn = getCases(text)
    if textReturn:
        return textReturn

    textReturn = getCities(text)
    if textReturn:
        return textReturn

    textReturn = getStates(text)
    if textReturn:
        print(len(textReturn))
        return textReturn

    textReturn = getHospitals(text)
    if textReturn:
        return textReturn

    textReturn = getNews(text)
    if textReturn:
        return textReturn

    return alternate_text


def getCases(country):
    # return selected item to the user
    object_country = pycountry.countries.get(name=country)
    if object_country:
        try:
            numberOfCases, deaths, recovered, newConfirmed, newRecovered, newDeaths \
                = casesDataSet.numberOfCasesInCountry(country)
        except ValueError:
            return "Too many values"
    else:
        return False
    testing_list = testing_data_country_wise(object_country.alpha_3, country)
    random_message = 'Stats for {} are\nCases: {}\nDeaths: {}\nRecovered: {}' \
                     '\nNew Confirmed: {}\nNew Recovered: {}\nNew Deaths: {}\n'.format(country, numberOfCases, deaths
                                                                                       , recovered, newConfirmed,
                                                                                       newRecovered, newDeaths)
    print(str(testing_list) + " this is printed")
    for testing_stat in testing_list:
        message = f"{testing_stat[0]} are\nCumulative tests: {testing_stat[1]}\n" \
                  f"Daily Count of test: {testing_stat[2]}\n"
        random_message += message
    return random_message


def getHospitals(locality):
    if 'news' in locality:
        return False
    listOfHospitals = HospitalLocation.hospitalLocationsOnCoordinates(locality)
    if listOfHospitals:
        stringOfHospitals = ''
        for hospitals in listOfHospitals:
            stringOfHospitals += str(hospitals) + '\n'
        return stringOfHospitals
    else:
        return False


def getNews(text):
    if 'news' not in text:
        return False

    listOfText = text.split()
    listOfArticles = []
    newsTexts = ''

    for word in listOfText:
        if pycountry.countries.get(name=word):
            listOfArticles = news.return_news(word)
            break

    if listOfArticles:
        return listOfArticles
    else:
        return False


def getCities(text):
    if 'hospitals' not in text:
        return False
    listOfText = text.split()
    list_of_tuples = []
    for word in listOfText:
        index = binary_search(state_list.city_list, word, 0)
        if index is not '':
            tuple_of_city = state_list.city_list[index]
            list_of_tuples.append(tuple_of_city)
    if not list_of_tuples:
        return False
    list_of_hospitals = []
    for city in list_of_tuples:
        hospitalData = indianData.beds_city_wise(city)
        message = hospitalDataOutput(city[0], hospitalData)
        list_of_hospitals.append(message)
    return list_of_hospitals



def getStates(text):
    kashmir = ''
    if 'Jammu & Kashmir' in text:
        print('entered jmammu')
        kashmir = 'Jammu and Kashmir'
        text.replace('Jammu & Kashmir', '')
        print(text)
    elif 'Jammu and Kashmir' in text:
        kashmir = 'Jammu and Kashmir'
        text.replace('Jammu and Kashmir', '')
    listOfText = text.split()
    listOfText.append(kashmir)
    if not len(listOfText) < 2:
        listOfText = findingTwoWordedStates(listOfText)
    stateInText = intersection(listOfText, state_list.state_list)
    if not stateInText:
        return False
    if len(stateInText) > 1:
        returningItem = []
        for state in stateInText:
            stateData = indianData.state_wise_numbers(state)
            # stateHospitals = indianData.beds_state_wise(state)
            random_message = initialDataOutput(state, stateData)
            returningItem.append(random_message)
        return returningItem
    else:
        stateData = indianData.state_wise_numbers(stateInText[0])
        # stateHospitals = indianData.beds_state_wise(stateInText[0])
        # if not stateHospitals:
        #     return False
        return initialDataOutput(stateInText[0], stateData)


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def changeJson(number):
    return "{:,}".format(number)


def messageGeneration(stateName, stateData, stateHospitals):
    random_message = initialDataOutput(stateName, stateData)
    random_message += hospitalDataOutput(stateName, stateHospitals)
    return random_message


def initialDataOutput(stateName, stateData):
    random_message = 'Stats for {} are\n' \
                     'Cases: ' \
                     '{}\nDeaths: {}' \
                     '\nDischarged: {}\n\n' \
        .format(stateName, changeJson(stateData['totalConfirmed']), changeJson(stateData['deaths']),
                changeJson(stateData['discharged']))
    return random_message


def hospitalDataOutput(stateName, stateHospitals):
    random_message = ''
    for hospital in stateHospitals:
        random_message += 'Hospitals in ' + stateName + ' are \n' \
                          'Name: {}' \
                          '\nCity: {}' \
                          '\nAdmission Capacity: {}' \
                          '\nHospital beds: {}' \
                          '\nOwner: {}\n\n'.format(hospital['name'], hospital['city'],
                                                   hospital['admissionCapacity'], hospital['hospitalBeds'],
                                                   hospital['ownership'])
    return random_message


def findingTwoWordedStates(list_of_words):
    i = 1
    while i < len(list_of_words):
        possible_state = list_of_words[i - 1] + ' ' + list_of_words[i]
        if possible_state in state_list.state_list:
            list_of_words[i] = possible_state
            list_of_words.pop(i-1)
        i = i + 1
    return list_of_words

x = getCases('India')
print(x)
