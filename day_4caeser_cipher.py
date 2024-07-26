#a-z 65-90
#a-z 97-122
#ord(your_letter)
#chr(your_code)

#Hints
#use is upper to decide which unicodes to work w
#add the key(number of characters to shift)
#if key is bigger or small than unicode than a,z,A, or Z, increase or decrease by 26

#recieve the message to encrypt and num of chars to shift
og_message = input("What message would you like to encrypt? ")
shift_num = input("By how many numbers would you like to shift your message? ")
#prep the message
secret_message =""
#cycle thru each char in the message
for char in og_message:
    #if a letter isnt a letter, keep as is
    if char.isalpha():

    #get the char code and add the shift number amount
        char_code = ord(char)
        char_code += shift_num
    #If uppercase then compare to uppercase unicodes
    if char.isupper():

       #if bigger than Z, subtract 26
       if char_code > ord("Z"):
           char_code -= 26
        #if smaller than A, add 26
       if char_code < ord("A"):
           char_code += 26
    else:
       if char_code > ord("z"):
           char_code -= 26
       if char_code > ord("a"):
           char_code += 26
    #convert from code to letter and add to message
    secret_message +=chr(char_code)
else:
    secret_message += char
#if not letter leave character as is 
print("Encrypted: ", secret_message)
#To decrypt the only thing that vhanges
