

"""colors  is the module which generates the color dictionary"""


color = {}                                  # declare a color dictionary
color['yellow']   = [1.0, 1.0, 0.0]         # fill each entry of the color dictionary with a list of three floats
color['blue']     = [0.0, 0.0, 1.0]
color['red']      = [1.0, 0.0, 0.0]
color['green']    = [0.0, 1.0, 0.0]
color['sienna']   = [0.627, 0.322, 0.176]
color['hotpink'] =  [1.0, 0.412, 0.706]

def print_available_colors():
    """This function prints all the available colors"""
    print('Available colors:')
    print('yellow')
    print('blue')
    print('red')
    print('green')
    print('sienna')
    print('hotpink')


print_available_colors()