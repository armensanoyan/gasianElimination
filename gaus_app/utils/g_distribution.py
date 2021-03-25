import operator

operations_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
operations = ['+','-','*','/','=']


matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

input_operator = '*'

def matsum(m1, m2, operation):
    if operation in '+-':
        operation_f = operations_dict[operation]

        if len(m1) == len(m2):
            result = [[operation_f(m1[i][j], m2[i][j]) for j in range(len(m1[i]))] for i in range(len(m1))]
            return result

    if operation == '*':
        multarr = [[sum(a*b for a,b in zip(m1_row,m2_col)) for m2_col in zip(*m2)] for m1_row in m1]

        return multarr