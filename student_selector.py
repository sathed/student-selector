#!/usr/bin/python3
from random import seed, randint
import calendar
import time

seconds_since_epoch = calendar.timegm(time.gmtime())

# These number correspond to the number in your AWS username.
students = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23"
]

seed(seconds_since_epoch)

# Winner #1
random_number = randint(0, len(students) - 1)
print("First winner is {}".format(students[random_number]))
students.pop(random_number)

# Winner #2
random_number = randint(0, len(students) - 1)
print("Second winner is {}".format(students[random_number]))
students.pop(random_number)

# Winner #3
random_number = randint(0, len(students) - 1)
print("Third winner is {}".format(students[random_number]))
