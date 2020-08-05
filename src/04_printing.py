"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
print('Y is: %f and Z is: %s' % (y, z))
# x is 10, y is 2.25, z is "I like turtles!"
print('X is: %i Y is: %g and Z is: %s' % (x, round(y, 2), z))
# Use the 'format' string method to print the same thing
print('X is: %s Y is: %s and Z is: %s' % (x, round(y, 2), z))
# Finally, print the same thing using an f-string
print(f'X is: {x} Y is: {round(y,2)} and Z is: {z}')