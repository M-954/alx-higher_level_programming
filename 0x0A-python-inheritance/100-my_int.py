#!/usr/bin/python3
'''
an implementation of the module 100-my_int
'''


class MyInt(int):
    '''
    implementation of MyInt which inherits from class int
    '''

    def __eq__(self, other):
        '''
        inverts the implementation of ==
        '''
        return super().__ne__(other)

    def __ne__(self, other):
        '''
        inverts the implementation of !=
        '''
        return super().__eq__(other)
