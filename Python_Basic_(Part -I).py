# https://www.w3resource.com/python-exercises/python-basic-exercises.php
# 1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are
import calendar

print(
    "Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a "
    "diamond in the sky. \nTwinkle, twinkle, little star, \n\t How I wonder what you are")


# 2. Write a Python program to get the Python version you are using
import sys
vers = sys.version
print('Python version: ' + vers)

print('Version info: ')
print(sys.version_info)

# 3. Write a Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print('Current date and time : ' + now.strftime('%Y - %m - %d %H:%M:%S'))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area
import math
r = float(input('Radius of the circle: '))
print('The are of the circle with radius ' + str(r) + ' is: ' + str(math.pi * r**2))

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space
# between them.
first_name = input('First name: ')
last_name = input ('Last name: ')

print(last_name + ' ' + first_name)

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a
# tuple with those numbers.
numbers = input('Write some comma separated number here: ')
list = numbers.split(",")
tuple = tuple(list)
print('List: ', list)
print('Tuple: ', tuple)

# 7. Write a Python program to accept a filename from the user and print the extension of that.
file_name = input('Filename: ')
file_extension = file_name.split('.')
print('The file extension is: ' + file_extension[-1])

# 8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red", "Green", "White", "Black"]
print(color_list[0] + ' ' + color_list[-1])
print('%s %s' % (color_list[0], color_list[-1]))

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print('The examination will start from: %i / %i /%i'% exam_st_date)

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
integer = int(input('Type an integer: '))
n1 = int('%s' % integer)
n2 = int('%s%s' % (integer, integer))
n3 = int('%s%s%s' % (integer, integer,integer))
print(n1 + n2 + n3)

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
print(abs.__doc__)
print(all.__doc__)

# 12. Write a Python program to print the calendar of a given month and year.
month = int(input('month: '))
year = int(input('year: '))
i = calendar.month(year, month, w=4, l=0.9)
print(i)


