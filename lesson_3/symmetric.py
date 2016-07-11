
def symmetric(matrix):
    N = len(matrix)
    for i in range(N):
        M = len(matrix[i])
        if N != M:
            return False
        for j in range(M):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False


def antisymmetric(matrix):
    N = len(matrix)
    for i in range(N):
        M = len(matrix[i])
        if N != M:
            return False
        for j in range(M):
            if matrix[i][j] == matrix[j][i] and matrix[j][i] != 0 and matrix[i][j] != 0:
                return False
    return True

print antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]])


# >>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
# >>> True

print antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2, 3]])
# >>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
# >>> False