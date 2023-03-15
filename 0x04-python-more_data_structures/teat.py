
matrix = [
        [1, 2, 3],
        [4, 5, 6]
        ]
listt = [[j** 2 for j in i] for i in matrix]

for i in listt:
    for j in i:
        print(j, end=', ')
    print()

