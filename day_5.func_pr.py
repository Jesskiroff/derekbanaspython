#Solve 4 x
# x+4 = 9
# x will always be the first val recieved and you'll only deal w addition
#recieve the str and split inconvert the str into ints
##convert the result into ints
#convert the result into str and join it to the string "X = "
#print()



# num1 = input(int("What is the x value? "))
# num2= input(int("What is the y value? "))
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)
    
    return "x = " + str(num2 -num2)

print(solve_eq("x + 4 = 9"))