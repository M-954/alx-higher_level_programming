#!/usr/bin/python3
class MyList(list):
    def __init__(self, elements=None):
        self.elements = elements or []
        if elements is not None:
            for i in elements:
                if type(i) is not int:
                    raise TypeError('all elements in the list must be integers')
        super().__init__(self.elements)
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
