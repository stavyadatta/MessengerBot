import random
import pycountry
import casesDataSet


def get_message(country):
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!",
                        "We're greatful to know you :)"]
    # return selected item to the user
    numberOfCases = ''
    deaths = ''
    if pycountry.countries.get(name=country):
        numberOfCases, deaths = casesDataSet.numberOfCasesInCountry(country)
    random_message = random.choice(sample_responses)
    random_message += ' cases {} and deaths {}'.format(numberOfCases, deaths)
    return random_message