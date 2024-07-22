#ask 4 a string
original_string = input("What is the original sentence? ")

#cinvert the string to uppercase
upper_string = original_string.upper()
#cnvert the string in2 a list
def Convert(string):
    li = list(string.split(" "))
    return li
print(Convert(upper_string))
#cycle thru the list 
    #get the 1st letter of th word and eliminate the newline
#add a newline