## Name: Connie Chen
## Student Number: 251086218
## Assignment: 4

from country import *


class CountryCatalogue:  # create class CountryCatalogue
    def __init__(self, countryFile):  # create constructor
        self._countryCat = {}  # create country catalogue dictionary

        with open(countryFile) as countryData:
            # skip the first line in the data files (i.e. the header)
            header = True
            for line in countryData:
                if header:
                    header = False
                else:
                    line = line.rstrip().replace(",", "").split("|")  # clean up data for future use
                    self._countryCat[line[0]] = Country(line[0], line[2], line[3], line[1])  # country, population, area, continent

    ## setter methods
    #
    def setPopulationOfCountry(self, country, new_pop):
        i = self._countryCat[country]
        i.setPopulation(new_pop)
        self._countryCat[country] = i

    def setAreaOfCountry(self, country, new_area):
        i = self._countryCat[country]
        i.setArea(new_area)
        self._countryCat[country] = i

    def setContinentOfCountry(self, country, new_continent):
        i = self._countryCat[country]
        i.setContinent(new_continent)
        self._countryCat[country] = i

    # method to find country. returns country object or None based on if the country name is in the country catalogue
    def findCountry(self, country):
        for i in self._countryCat.values():
            if i.getName() == country.getName():
                return i
        return None

    # adds new country to catalogue
    def addCountry(self, countryName, pop, area, cont):
        newCntry = Country(countryName, pop, area, cont)
        if self.findCountry(newCntry) is None:
            self._countryCat[newCntry.getName()] = newCntry
            return True
        # country already exists in catalogue
        else:
            print("This country already exists")
            return False

    # prints entire country catalogue with
    def printCountryCatalogue(self):
        for x in self._countryCat:
            print(self._countryCat[x].__repr__())

    # saves country catalogue to a file specified by fname
    def saveCountryCatalogue(self, fname):
        newCountryCat = {}  # create new dictionary to store data
        try:
            file = open(fname, "w")  # open file to write in
            sorted_keys_Catalogue = sorted(self._countryCat.keys())  # sort countries in catalogue in alphabetical order

            for j in sorted_keys_Catalogue:
                newCountryCat[j] = self._countryCat.get(j)
            file.write("Country|Continent|Population|Area\n")

            for k in newCountryCat.values():
                file.write("{}|{}|{}|{}\n".format(k.getName(), k.getContinent(), k.getPopulation(), k.getArea()))
            file.close()

            return len(newCountryCat)

        except IOError:
            print("The file already exists")
            return -1

