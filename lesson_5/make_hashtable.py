# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    return [[] for i in range(nbuckets)]

print make_hashtable(1)
print make_hashtable(5)