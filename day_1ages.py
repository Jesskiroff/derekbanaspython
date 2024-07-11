#IF AGE IS 5 GO TO KINDERGADEN
#AGES 6-17 GOES TO GRADES 1-12
#if age is greater than 17, say go to college
#try to complet w 10 lines or less
age = eval(input("Enter age: "))
if (age == 5):
    print("goes to kindergarden")
elif (age > 5) and (age <= 17):
    grade = age -5
    print("goes to {} grade".format(grade))
elif (age > 17 ) and (age <= 22):
    print("goes to college")
else:
    print("not in school")