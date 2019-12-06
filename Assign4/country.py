## Name: Connie Chen
## Student Number: 251086218
## Assignment: 4


class Country:  # create the class Country

    def __init__(self, name, pop, area, continent):  # create construtor

        # instance variables
        self._countryName = name
        self._population = pop
        self._area_of_country = area
        self._continentName = continent

    ## getter methods
    #
    def getName(self):  # gets country name
        if self._countryName == "":
            return ""
        else:
            return self._countryName

    def getPopulation(self):
        if self._population == "":
            return str(0)
        else:
            return self._population  # gets population of the country

    def getArea(self):
        if self._area_of_country == "":
            return str(0)
        else:
            return self._area_of_country  # gets area of the country

    def getContinent(self):
        if self._continentName == "":
            return ""
        else:
            return self._continentName  # get continent

    ## setter methods
    #
    def setPopulation(self, pop):
        self._population = str(pop)  # sets the population of the country

    def setArea(self, area):
        self._area_of_country = str(area)  # sets area of the country

    def setContinent(self, cont):
        self._continentName = cont  # sets the name of the continent

    ## repr method (returns string)
    def __repr__(self):
        return '{} (population: {}, size: {}) in {}'.format(self._countryName, self._population, self._area_of_country, self._continentName)
