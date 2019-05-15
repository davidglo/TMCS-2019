"""colours is a simple module for creating a colour dictionary."""

from random import uniform

colour_palette = {}     # Defines a dictionary containing the colours as keys and their colour3f reference
colour_palette["blue"] = [0.21, 0.21, 0.81]
colour_palette["yellow"] = [1.00, 1.00, 0.00]
colour_palette["green"] = [0.00, 1.00, 0.00]
colour_palette["sienna"]   = [0.627, 0.322, 0.176]
colour_palette["hotpink"] =  [1.0, 0.412, 0.706]

def printAvailableColours():
    """This function prints all available colours within the colours dictionary."""
    for key in colour_palette.keys():
        print(str(key))


def random_colour():

    colour = []

    for i in range(3):
        colour_index = uniform(0, 1)
        colour.append(colour_index)

    return colour