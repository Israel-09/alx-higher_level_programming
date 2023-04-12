#!/usr/bin/python3
''' module on python inheritance
'''


class MyList(list):
    
    def print_sorted(self):
        '''
        prints a sorted list of integers
        '''
        print(sorted(self))

if __name__ == '__main__':
    x = MyList()
    print(dir(x))
    x.append('z')
    x.append('Z')
    print(x)
    x.print_sorted()
