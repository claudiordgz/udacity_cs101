# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

def is_identity_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        M = len(matrix[0])
        if N != M:
            return False
        if matrix[i][i] != 1:
            return False
        for j in range(M):
            if i != j:
                if matrix[i][j] != 0:
                    return False
    return True



# Test Cases:

matrix1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
print is_identity_matrix(matrix1)
# >>>True

matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

print is_identity_matrix(matrix2)
# >>>False

matrix3 = [[2, 0, 0],
           [0, 2, 0],
           [0, 0, 2]]

print is_identity_matrix(matrix3)
# >>>False

matrix4 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print is_identity_matrix(matrix4)
# >>>False

matrix5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print is_identity_matrix(matrix5)
# >>>False

matrix6 = [[1, 0, 0, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]

print is_identity_matrix(matrix6)
# >>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
# >>>False

print("");print("");print("");print("");

# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    previous = int(string[0])
    result = [previous]
    sub = []
    for char in string[1:]:
        current = int(char)
        if current <= previous:
            sub.append(current)
        else:
            if sub:
                result.append(sub)
                sub = []
            result.append(current)
            previous = current
    if sub:
        result.append(sub)
    return result

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
