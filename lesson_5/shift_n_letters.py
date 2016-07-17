# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    begin = ord('a')
    end = ord('z')
    char = ord(letter)
    if (char + n) > end:
        return chr(begin + (n - (end - char)) - 1)
    elif (char + n) < begin:
        return chr(end + (n + (char - begin)) + 1)
    else:
        return chr(char + n)

print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('a', -1)
#>>> z