# #ask 4 a string
# original_string = input("What is the original sentence? ")

# #cinvert the string to uppercase
# original_string = original_string.upper()
# #cnvert the string in2 a list
# '''def Convert(string):
#     li = list(string.split(" "))
#     return li
# print(Convert(original_string))'''
# list_of_words = original_string.split()
# #cycle thru the list 
# print(list_of_words)
# for word in list_of_words:
#     #get the 1st letter of th word and eliminate the newline
#     print(word[0], end="")

# #add a newline
# print()




#ask 4 a string
og_str = input("What is the og sentence? ")
#convert the str in2 uppercase
og_str = og_str.upper()
#convert the string into list
str_into_li = og_str.split()
#cycle thru the list
for word in str_into_li:
    #get the 1st letter of th word and eliminate the newline
    print(word[0], end ='')
#add a new line
print()