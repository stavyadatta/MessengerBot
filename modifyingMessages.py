import casesDataSet
import HospitalLocation
import pycountry
import news


def textDecider(text):
    textReturn = getCases(text)
    if textReturn:
        return textReturn

    textReturn = getHospitals(text)
    if textReturn:
        return textReturn

    textReturn = getNews(text)
    if textReturn:
        return textReturn

    return "Didn't get your text, please try again later"


def getCases(country):
    # return selected item to the user
    if pycountry.countries.get(name=country):
        try:
            numberOfCases, deaths = casesDataSet.numberOfCasesInCountry(country)
        except ValueError:
            return "Too many values"
    else:
        return False
    random_message = 'Stats for {} are\nCases: {}\nDeaths: {}'.format(country, numberOfCases, deaths)
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
        for i in listOfArticles:
            newsTexts += str(i) + '\n'
        return newsTexts
    else:
        return False
