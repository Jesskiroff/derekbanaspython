#name = input('What is your name? ')
#print out helllo followed by name they entered
#print('Hello', name)
#var names can start w letters or _


#ask user to input 2 values and store them in variables num1 and num2
num1, num2 = input("enter 2 numbers: ").split() #if you put 2 nuber w a spca ein between, it'll know that there's a split
#convert strings in2 reg nums and int
num1 = int(num1)
num2= int(num2)
# add the values entered and store in sum
sum = num1 + num2
# subtract values and store in difference
difference = num1 - num2
# multiply values and store in product
product = num1 * num2
# divide the value and store in quotient
quotient = int(num1 / num2)

remainder = num1 % num2
print('{} + {} = {}'.format(num1,num2,sum))
print('{} - {} = {}'.format(num1,num2,difference))
print('{} * {} = {}'.format(num1,num2,product))
print('{} / {} = {}'.format(num1,num2,quotient))
print('{} % {} = {}'.format(num1,num2,remainder))