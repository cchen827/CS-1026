## Name: Connie Chen
## Student Number: 251086218
## Assignment: 4

from catalogue import *


def processUpdates(cntryFileName, updateFileName):  # create function processUpdates that can be tested with main.py
    checkCountry = True
    checkUpdate = True

    while checkCountry:  # while true

        # try to open country file and provide exception if the country file does not exist
        try:
            open(cntryFileName, "r")
        except IOError:
            if input("Country file does not exist. Quit? (Y/N): ") == "N":
                cntryFileName = input("Please enter new country file: ")
            else:
                # create output.txt if update is unsuccessful and write in it to let user know
                output_file = open("output.txt", "w")
                output_file.write("Update Unsuccessful\n")
                output_file.close()
                return False
        checkCountry = False
    cntry_File = CountryCatalogue(cntryFileName)

    while checkUpdate:  # while true

        # try to open update file and provide exception if the update file does not exist
        try:
            updatedFile = open(updateFileName, "r")
        except IOError:
            if input("Update file does not exist. Quit? (Y/N): ") == "N":
                updateFileName = input("Please enter new update file: ")
                continue
            else:
                # create output.txt if update is unsuccessful and write in it to let user know
                output_file_2 = open("output.txt", "w")
                output_file_2.write("Update Unsuccessful\n")
                output_file_2.close()
                return False

        # format data in updatedFile to be used later
        for line in updatedFile:
            line = line.rstrip().replace(",", "").split(";")
            newContinent = ""
            newPopulation = ""
            newArea = ""

            country_name = line[0]
            country = Country(country_name, None, None, None)  # leave space in tuple for updates (pop, area, continent)
            find_country = cntry_File.findCountry(country)

            if find_country is None:  # if country is not in catalogue
                for i in line:
                    if i[:2] == "P=":
                        newPopulation = i[2:]
                    elif i[:2] == "A=":
                        newArea = i[2:]
                    elif i[:2] == "C=":
                        newContinent = i[2:]
                cntry_File.addCountry(country_name, newPopulation, newArea, newContinent)  # add new country with updated population, area, and continent

            else:
                for j in line:  # if country is in catalogue
                    if j[:2] == "P=":
                        newPopulation = j[2:]
                        cntry_File.setPopulationOfCountry(country_name, newPopulation)  # update with new population
                    elif j[:2] == "A=":
                        newArea = j[2:]
                        cntry_File.setAreaOfCountry(country_name, newArea)  # update with new area of country
                    elif j[:2] == "C=":
                        newContinent = j[2:]
                        cntry_File.setContinentOfCountry(country_name, newContinent) # update with new continent of country

        cntry_File.saveCountryCatalogue("output.txt")  # export updated data to output.txt
        checkUpdate = False

    return True

