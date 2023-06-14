#!/usr/bin/python3

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

def pascal_triangle(n):
    matrix = []
    layer = []
    for i in range(n):
        layer = layer[:]
        layer = []
        for j in range(i + 1):
            if j == i:
                layer.append(1);
                matrix.append(layer)
                break;
            elif j == 0:
                layer.append(1);
            else:
                num1 = matrix[i - 1][j - 1]
                num2 = matrix[i - 1][j]
                layer.append(num1 + num2)
    return (matrix)

print_triangle(pascal_triangle(8))
