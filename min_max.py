print ("How many integers would you like to enter?")
iteration_count = int(input())
print ("Please enter iteration_count integers.")
integer = int(input ())
min = integer
max = integer
for num in range (1, iteration_count):
    integer = int(input ())
    if integer < min:
        min = integer
    elif integer > max:
        max = integer
print ("min:", min)
print ("max:", max)
