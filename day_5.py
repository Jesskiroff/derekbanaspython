# def add_numbers(num1, num2):
#     return num1+ num2

# print ("5 + 4 = ", add_numbers(5,4))



# def change_name(name):
#     return "Mark"
 
# name = "Tom"

# name = change_name(name)
# print (name)

# glb_name = "Sally"

# def change_name(): 
#     global glb_name
#     glb_name = "Sammy"

# change_name()
# print(glb_name)


# Solve for x
# x + 4 = 9
# x will always be the 1st value recieved and you only will deal w addition


# receive the string and split the string into variables
#convert the strings into ints
#convert the result into a string 
#convert the result into a string and join it to the string "X = "
#print()

def solve_equation(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)

# add_these = input("What two numbers would you like to add today? ")
# add_these_split = add_these.split(",")
