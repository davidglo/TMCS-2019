"""colors is a simple module for creating a color dictionary"""
from random import randint

color = {}  # declare a color dictionary
color['yellow'] = [1.0, 1.0, 0.0]  # fill each entry of the color dictionary with a list of three floats
color['blue'] = [0.0, 0.0, 1.0]
color['red'] = [1.0, 0.0, 0.0]
color['green'] = [0.0, 1.0, 0.0]
color['sienna'] = [0.627, 0.322, 0.176]
color['hotpink'] = [1.0, 0.412, 0.706]

def printAvailableColors():
    """This function prints all available colors"""
    print('\tyellow' )
    print('\tblue'   )
    print('\tred'    )
    print('\tgreen'  )
    print('\tsienna' )
    print('\thotpink')

def getRandColorString():
    """Returns RGB for one of the colors"""
    randnum = randint(0,5)
    if randnum == 0:
        return 'yellow'
    elif randnum == 1:
        return 'blue'
    elif randnum == 2:
        return 'red'
    elif randnum == 3:
        return 'green'
    elif randnum == 4:
        return 'sienna'
    else:
        return 'hotpink'

if __name__ == "__main__":
    # only run this code if colors.py is run as the top-level function
    # ignore if colors.py is imported as a module
    print('executing colors.py as the main routine')
    print('we have definitions of:')
    printAvailableColors()