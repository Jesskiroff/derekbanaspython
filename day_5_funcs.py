def add_numbers(num1, num2):
    return num1 + num2

#print("5 + 4 = ", add_numbers(5,4))

'''LOCAL VARIABLES'''

def assign_name():
    name = "Albert"
assign_name()

def change_name(name):
    name = "Mark"
name = "Ryan"
change_name(name)
print(name)

def name_change(name):
    return "Mark"
name = "Allen"
name = name_change(name)
print(name)