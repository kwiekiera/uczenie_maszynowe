import requests
import argparse

class Brewery:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)
        
    def __str__(self):
        return("Id: {}\nNazwa: {}\nTyp: {}\nUlica: {}\nAdres 2: {}\nAdres3: {}\nMiasto: {}\nStan: {}\nProwincja: {}\nKod pocztowy: {}\nKraj: {}\nDł. geograficzna: {}\nSzerokosć geograficzna: {}\nNr telefonu: {}\nURL: {}\nData modyfikacji: {}\nData utworzenia: {}"
               .format(self.id, self.name, self.brewery_type, self.street, self.address_2, self.address_3, self.city, self.state, self.county_province, self.postal_code, self.country, self.longitude, self.latitude, self.phone, self.website_url, self.updated_at, self.created_at))
        
def showBreweries(city=""):
    breweriesList = []
    if city == None:
        response = requests.get("https://api.openbrewerydb.org/breweries?page=1")
    else:
        response = requests.get("https://api.openbrewerydb.org/breweries?page=1&by_city={}".format(city))
    breweries = response.json()
    for i in range(len(breweries)):
        breweriesList.append(Brewery(breweries[i]))
        
    for i in range(len(breweriesList)):
        print(breweriesList[i])
        print()
        
#zad 7
showBreweries()

#zad 8
parser = argparse.ArgumentParser()
parser.add_argument('--city', type=str, required=False)
args = parser.parse_args()
showBreweries(args.city)