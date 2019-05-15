"""colors is a simple module for creating a color dictionary"""

color = {'red':[1,0,0],'green':[0,1,0],'blue':[0,0,1],"mix":[0.5,0.5,0.5]}
color['yellow'] = [1.0, 1.0, 0.0]
color['sienna'] = [0.627, 0.322, 0.176]
color['hotpink'] = [1.0, 0.412, 0.706]

def printColorOptions():
    """This function prints all available colors within our dictionary"""
    print ("Colors Available: ")
    for key in color.keys():
        print (key,": ", color[key])


if __name__ == "__main__":
    # only run this code if colors.py is run as the top-level function
    # ignore if colors.py is imported as a module
    print('executing colors.py as the main routine')
    print('we have definitions of:')
    printAvailableColors()

