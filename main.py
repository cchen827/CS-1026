# import necessary functions from files
from Assignments.Assign2.volumes import cubeVolume, pyramidVolume, ellipsoidVolume
from Assignments.Assign2.summarize import summarize

# initialize user input
shapeInput = 0

# the following variables store output volumes into list
cubeVol = 0
pyramidVol = 0
ellipsoidVol = 0

# initialize list from summarize.py
clist = []
plist = []
elist = []


def formatInput(textLine):  # error trapping for capitals in user input below
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine


testNumber = int(input("Please input 1, 2, or 3 for test case number."))  # first, prompt user for test case number
while shapeInput != "q":  # loops request until the user enters "quit"
    shapeInput = input("Please type \"c\" or\"cube\" for cube, \"p\" or \"pyramid\" for pyramid, \"e\" or \"ellipsoid\" for ellipsoid, \"q\" or \"quit\" to quit ")  # second, prompt user for shape
    shapeInput = formatInput(shapeInput)

    if shapeInput == "c" or shapeInput == "cube":
        s = float(input("Please input a value for the side length of a cube: "))  # ask user to input side length of cube
        cubeVolume(s)
        cubeVol = cubeVolume(s)
        clist.append(cubeVol)  # add cube volume to array for final statement
        clist.sort()  # sort in ascending order

    elif shapeInput == "p" or shapeInput == "pyramid":
        b = float(input("Please input a value for the base length of a pyramid: "))  # ask user to input base length of pyramid
        h = float(input("Please input a value for the height of a pyramid: "))  # ask user to input height of pyramid
        pyramidVolume(b, h)
        pyramidVol = pyramidVolume(b, h)
        plist.append(pyramidVol)  # add pyramid volume to array for final statement
        plist.sort()

    elif shapeInput == "e" or shapeInput == "ellipsoid":
        r1 = float(input("Please input a value for radius one of an ellipsoid: "))  # ask user to input radius one of ellipsoid
        r2 = float(input("Please input a value for radius two of an ellipsoid: "))  # ask user to input radius two of ellipsoid
        r3 = float(input("Please input a value for radius three of an ellipsoid: "))  # ask user to input radius three of ellipsoid
        ellipsoidVolume(r1, r2, r3)
        ellipsoidVol = ellipsoidVolume(r1, r2, r3)
        elist.append(ellipsoidVol)  # add ellipsoid volume to array for final statement
        elist.sort()

    elif shapeInput == "q" or shapeInput == "quit":
        break

    else:
        print("The input is invalid, please try again.")

summarize(clist, plist, elist, testNumber)  # CREATE TEST CASE FILES

print("You have come to the end of the session.")

# START END STATEMENT

if len(clist) == len(plist) == len(elist) == 0:  # no input for any shape
    print("You did not perform any volume calculations")

else:  # when there is input for shapes
    print("The volumes calculated for each shape are: ")

    if len(clist) != 0:
        print("Cube: ", clist)
    else:
        print("Cube: No shapes entered.")

    if len(plist) != 0:
        print("Pyramid: ", plist)
    else:
        print("Pyramid: No shapes entered.")

    if len(elist) != 0:
        print("Ellipsoid: ", elist)
    else:
        print("Ellipsoid: No shapes entered.")
