#Problem : recieve miles and convert to kilometers
#kilometers = miles * 1.60934
#Enter Miles 5
#% miles equals 8.04 kilometers

# miles= int(input("How many miles are we converting to kilometers today? "))
# kilometers = miles * 1.60934

# print(f"{miles} miles = {kilometers} kilometers")


#store user input of 2 numbers and operator of choice 
num1,operator, num2 = input("enter 2 numbers and the operator ").split()
# convert strings in2 integers
num1 = int(num1)
num2 = int(num2)
#if + then we need to provide output based on addition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))
else:
    print("{} / {} = {}".format(num1, num2, num1/num2))

#print the result