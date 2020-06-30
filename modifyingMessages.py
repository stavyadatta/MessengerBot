import pycountry
import casesDataSet
import HospitalLocation


def textDecider(text):
    if getCases(text):
        return getCases(text)
    elif getHospitals(text):
        return getHospitals(text)
    else:
        return "Didn't get your text, please try again later"


def getCases(country):
    # return selected item to the user
    if pycountry.countries.get(name=country):
        numberOfCases, deaths = casesDataSet.numberOfCasesInCountry(country)
    else:
        return False
    random_message = ' cases {} and deaths {}'.format(numberOfCases, deaths)
    return random_message


def getHospitals(locality):
    listOfHospitals = HospitalLocation.hospitalLocationsOnCoordinates(locality)
    if listOfHospitals:
        stringOfHospitals = ''
        for hospitals in listOfHospitals:
            stringOfHospitals += str(hospitals) + '\n'
        return stringOfHospitals
    else:
        return False
