#!/usr/bin/python3
from random import seed, randint
import calendar
import time

# Get the number of seconds since epoch.
seconds_since_epoch = calendar.timegm(time.gmtime())

# These number correspond to the number in your AWS username.
students = []
num_students = 23
# Create a list of AWS username numbers
for i in range(1, num_students+1):
    students.append(str(i))

# Seconds since epoch as the seed.
# This will inject a new random seed every second.
seed(seconds_since_epoch)

# Winner #1
random_number = randint(0, len(students) - 1)
print("First winner is {}".format(students[random_number]))
# Prevent duplicates.
students.pop(random_number)

# Winner #2
random_number = randint(0, len(students) - 1)
print("Second winner is {}".format(students[random_number]))
students.pop(random_number)

# Winner #3
random_number = randint(0, len(students) - 1)
print("Third winner is {}".format(students[random_number]))
