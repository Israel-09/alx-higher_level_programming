#!/usr/bin/python3
''' module on python inheritance
'''


class MyList(list):
    '''class that inherits list object'''

    def print_sorted(self):
        '''
        prints a sorted list of integers
        '''
        print(sorted(self))
