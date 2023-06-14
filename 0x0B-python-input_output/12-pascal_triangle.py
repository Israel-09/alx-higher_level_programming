#!/usr/bin/python3
'''script on pascal tringle'''


def pascal_triangle(n):
    '''
    returns a list of list of pascal triange

    Args:
        n (int): number up to which it prints

    Return:
            a matrix of pascal triangle
    '''
    matrix = []
    layer = []
    if n <= 0:
        return (matrix)

    for i in range(n):
        layer = layer[:]
        layer = []
        for j in range(i + 1):
            if j == i:
                layer.append(1)
                matrix.append(layer)
                break
            elif j == 0:
                layer.append(1)
            else:
                num1 = matrix[i - 1][j - 1]
                num2 = matrix[i - 1][j]
                layer.append(num1 + num2)
    return (matrix)
