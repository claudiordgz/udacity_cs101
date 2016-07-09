seven_days = 60 * 24 * 7 * 7
print(seven_days)

speed_of_light = 299792458   # meters per second
centimeters = 100            # one meter is 100 centimeters
nanosecond = 1.0/1000000000  # one billionth of a second
print(speed_of_light * centimeters * nanosecond)

print(speed_of_light * centimeters * nanosecond)

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
href='<a href='
start_link = page.find(href)
real_start_link = start_link+len(href)+1
end_link = page.find('"', real_start_link)
url=page[real_start_link:end_link]
print(url)

text = "all zip files are zipped"

# ENTER CODE BELOW HERE
print(text.find('zip', text.find('zip')))

marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

begin_replace = line.find(marker)
line = line[:begin_replace] + replacement + line[begin_replace + len(marker):]
print(line)

print 10/4.0
print 10/4
print 10.0/5
print 10*1.0/4
print 10/5
print 10/50

word = "madam"
word2 = "madman"

def is_palindrome(word):
    return word.find(word[::-1])
is_palindrome_str = is_palindrome(word)
is_palindrome_str_two = is_palindrome(word2)
print(is_palindrome_str)
print(is_palindrome_str_two)

i =0
while i != 10:
    i = i + 1
    print(i)


def print_numbers(n):
    for i in range(1,n+1):
        print(i)

print_numbers(3)

print("separator")

def loop(n, acc):
    if n == 1:
        return acc
    else:
        return loop(n-1, acc * n)

def factorial(n):
    return loop(n, 1)

print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(42))
print(factorial(52))

def factorial_two(n):
    acc = 1
    for i in reversed(range(1, n+1)):
        acc = acc * i
    return acc

print(factorial_two(4))
print(factorial_two(5))
print(factorial_two(6))
print(factorial_two(42))


def stamps(n):
    retA = n / 5
    b = n % 5
    retB = b / 2
    retC = 0 if b == 2 else retB % 2
    return retA, retB, retC

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
print stamps(42)
print stamps(68)


def fix_machine(debris, product):
    return product if all([letter in debris for letter in product]) else "Give me something that's not useless next time."

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'

from datetime import datetime, date

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    dt = date(year1, month1, day1)
    dt2 = date(year2, month2, day2)
    return (dt2 - dt).days


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()



def print_abacus(value):
    for l in str(value).zfill(10):
        m = ('0' * (5 - (int(l) - 5)), '0' * (int(l) - 5), '', '*****') if int(l) > 5 else ('00000', '', '*' * (5 - int(l)), '*' * int(l))
        print('|' + m[0] + m[2] + '   ' + m[1] + m[3] + '|')



###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|

def jungle_animal(animal, my_speed):
    if animal == 'zebra': print("Try to ride a zebra!")
    elif animal == 'cheetah':
        if my_speed > 115:
            print("Run!")
        else:
            print("Stay calm and wait!")
    else:
        print("Introduce yourself!")


jungle_animal('cheetah', 30)
#>>> "Stay calm and wait!"

jungle_animal('gorilla', 21)
#>>> "Introduce yourself!"

def nextDay(year, month, day):
    if day == 30:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
    else:
        return year, month, day + 1

print(nextDay(2012, 1, 1))
print(nextDay(2012, 4, 30))
print(nextDay(2012, 12, 1))
print(nextDay(1999, 12, 30))
print(nextDay(2012, 12, 30))


def daysBetweenDatesTwo(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0
    i = str(year1) + str(month1) + str(day1)
    end = str(year2) + str(month2) + str(day2)
    y, m, d = year1, month1, day1
    while i != end:
        days += 1
        y, m, d = nextDay(y, m, d)
        i = str(y) + str(m) + str(d)
    return days


def test_two():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3)]

    for (args, answer) in test_cases:
        result = daysBetweenDatesTwo(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test_two()
