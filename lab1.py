
import constant

# !!!Statements and comments!!!

a = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)

# -----------------------------------------------------------------------------------

for i in range(1, 11):
    print(i)
    if i == 5:
        break

    if True:
        print('Hello')
        a = 5

#  zwykły komentarz
#  zrobiony
#  dla funu


def double(num):
    # Function to double value
    return 2*num


print(double.__doc__)

# !!!python Variables!!!

# -----------------------------------------------------------------------------------

number = 10
number = 1.1

website = "apple.com"
print(website)

#  assigning a new value to website
website = 'programiz.com'

print(website)

# -----------------------------------------------------------------------------------

a, b, c = 5, 3.2, "Hello"

print(a)
print(b)
print(c)


x = y = z = 'same'

print(x)
print(y)
print(z)


# snake_case
# camelCase
# current_salary
# never use speacial symbols like !, @, #

# -----------------------------------------------------------------------------------

a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12c  # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# -----------------------------------------------------------------------------------

strings = "This is python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(raw_str)

# -----------------------------------------------------------------------------------

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is:", x)
print("y is:", y)
print("a:", a)
print("b:", b)

# -----------------------------------------------------------------------------------

drink = "Available"
food = None


def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)


menu(drink)
menu(food)

# -----------------------------------------------------------------------------------

fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

# !!!python Data Types!!!

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))

# -----------------------------------------------------------------------------------

a = [5, 10, 15, 20, 25, 30, 35, 40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

a = [1, 2, 3]
a[0] = 5
a[1] = 7.5
a[2] = 10
print(a)

# -----------------------------------------------------------------------------------

t = (5, 'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
# t[0] = 10 ==> 'tuple' object does not support assingment

# -----------------------------------------------------------------------------------

s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# s[5] = 'd'   ==> Strings are immutable in Python

# -----------------------------------------------------------------------------------

a = {5, 2, 3, 1, 4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

# -----------------------------------------------------------------------------------

a = {1, 2, 2, 3, 3, 3}  # ==> eliminate duplicates
print(a)

# -----------------------------------------------------------------------------------

# >>> a = {1,2,3}
# >>> a[1]
# Traceback (most recent call last):
#   File "<string>", line 301, in runcode
#   File "<interactive input>", line 1, in <module>
# TypeError: 'set' object does not support indexing

# -----------------------------------------------------------------------------------

d = {1: 'value', 'key': 2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
# print("d[2] = ", d[2])

# -----------------------------------------------------------------------------------

# Conversion from float to int will truncate the value (make it closer to zero).
a = int(10.6)
print(a)
# 10
a = int(-10.6)
print(a)
# -10

# Conversion to and from string must contain compatible values.
a = float('2.5')
print(a)
# 2.5
a = str(25)
print(a)
# '25'
# >>> int('1p')

# Traceback (most recent call last):
#   File "<string>", line 301, in runcode
#   File "<interactive input>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '1p'

# We can even convert one sequence to another.

a = set([1, 2, 3])
print(a)
# {1, 2, 3}
a = tuple({5, 6, 7})
print(a)
# (5, 6, 7)
a = list('hello')
print(a)
# ['h', 'e', 'l', 'l', 'o']

# To convert to dictionary, each element must be a pair:
a = dict([[1, 2], [3, 4]])
print(a)
# {1: 2, 3: 4}
a = dict([(3, 26), (4, 44)])
print(a)
# {3: 26, 4: 44}
