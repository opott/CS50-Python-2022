# get the expression from the user
expression = input("Enter an expression: ")

# split the expression into 3 variables
x, y, z = expression.split(" ")

# convert the numbers into floats
x = float(x)
z = float(z)

# determine what operation to use and perform the calculation
if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
    print("Invalid operation")

# convert result to a float and print it
result = float(result)
print(result)