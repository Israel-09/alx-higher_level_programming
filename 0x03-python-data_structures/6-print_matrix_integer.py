#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for s_list in matrix:
        for j in range(len(s_list)):
            print('{}'.format(s_list[j]), end='')
            if len(s_list) - 1 == j:
                print('', end='')
            else:
                print(' ', end='')
        print()
