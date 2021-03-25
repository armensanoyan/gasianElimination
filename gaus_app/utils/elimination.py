import copy
from random import randrange 
# n = int(input('write dimentions: '))
n =4

def generate(n):
    A = [[int(randrange(1, n*(n+1))) for j in range(n+1)] for i in range(n)]
    return A

def approxiamtion(matrix):
    return [[round(element, 3) for element in row] for row in matrix]

def elimination(A):
    steps = [] 
    steps.append({
        'matrix': copy.deepcopy(approxiamtion(A)),
        'comment': 'initial matrix'
    })
    n = len(A)

    for i in range(0, n):
        # check if there are any 0 pivot values
        if A[i][i] == 0:
            print("pivot values can't be zero")
            return {
                'result': None,
                "error" : "matrix doesn't have solution"
            }

        # search for max in this col
        max_value = abs(A[i][i])
        max_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > max_value:
                max_value = abs( A[j][i])
                max_row = j

        for k in range(i, n + 1):
            tmp = A[max_row][k]
            A[max_row][k] = A[i][k]
            A[i][k] = tmp
        print(f'the row with biggest {round(i)}th element is {[round(e) for e in A[i]]}')
        if i != 0:
            print(f'Swaping {i} row with {i} row')
        if max_row != i:
            steps.append({
                'matrix':copy.deepcopy(approxiamtion(A)),
                'comment': f'Swaping row {round(i)} with row {round(max_row)}'
            })

        # Make all rows below this one 0
        for j in range(i+1, n):
            c = -A[j][i]/A[i][i]
            for k in range(i, n+1):
                if k==i:
                    print(f"make A[{j}][{k}]'s value 0 ")
                    A[j][k] = 0
                else:
                    A[j][k] += c*A[i][k]
        
        steps.append({
            'matrix': copy.deepcopy(approxiamtion(A)),
            'comment': f'elements below {A[i][i]} made zero'
        })

    # Solve the equasion
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(n-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    
    steps.append({
            'matrix': x,
            'comment': f'Got the result'
        })

    return {
        'result': steps,
        'error': None
    }

