#!/usr/bin/python3
'''
A module of 1-my_list
'''


class MyList(list):
    '''
    A class MyList from class list


    atrributes:
    elements - the elements of the list
    raises:
    TypeError - if element is not an integer

    prints out the sorted elements of list
    '''
    def __init__(self, elements=None):
        self.elements = elements or []
        if elements is not None:
            for i in elements:
                if type(i) is not int:
                    raise TypeError('all elements in the '
                                    'list must be integers')
        super().__init__(self.elements)

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
