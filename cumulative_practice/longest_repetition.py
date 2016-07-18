# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(l):
    previous = -1
    count = 0
    list_of_reps = []
    list_type = False
    for idx, el in enumerate(l):
        hash = el
        if isinstance(el, list):
            hash = ''.join([str(i) for i in el])
            list_type = True
        if previous == -1:
            previous = hash
            count = 1
            list_of_reps.append([hash, count])
        else:
            if previous == hash:
                count += 1
                list_of_reps[-1][1] = count
            else:
                count = 1
                previous = hash
                list_of_reps.append([hash, count])
    largest = -1
    element = None
    for el in list_of_reps:
        if el[1] > largest:
            largest = el[1]
            element = el[0]
    if list_type:
        element = [int(i) for i in element]
    return element



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([[1], [2,2], [2,2], [2,2], [3,3,3]])
# [2,2]

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
#