"""colors is a simple module for creating a color dictionary"""

color = {}
color['red'] = [255, 0, 0]
color['blue'] = [0, 0, 255]
color['green'] = [0, 255, 0]
color['white'] = [255, 255, 255]

def printAvailableColors():
    """This function prints all available colors within our dictionary"""
    for i in list(color.keys()):
        print(i)




if __name__ == "__main__":
    # only run this code if colors.py is run as the top-level function
    # ignore if colors.py is imported as a module
    print('executing colors.py as the main routine')
    print('we have definitions of:')
    printAvailableColors()
