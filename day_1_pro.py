#diff outputs based on age
#1-18 -> imp 
#21, 50, > 65  -> imp 
#all others -> not imp

#receive age and store in age
age = eval(input("Enter age "))
# If age is both greater than or eqaul to 1 and less than 18 -imp
if (age>= 1) and (age <= 18):
    print ("important bday")
elif (age == 21) or (age == 50):
    print("important bday")
elif not (age < 65):
    print("important bday")
else:
    print("not imp :(")