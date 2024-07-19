# Enter a string to hide the unicode : Hide
#secret message : 34567890
#print Original message: hide

#Input enter a string to hide in uppercae
normal_string = input("Enter a string to hide in uppercase : ")
#cycle thru each character in the string
secret_string = ''
#store each character code in a new string
for char in normal_string: 
#print " secret message : 3467890"
    secret_string += str(ord(char))
#cycle thru each character code 2 at each time by inrementing by 2 each time
print("Secret message", secret_string)
#get the 1st and 2nd for the 2 digit number 
normal_string += ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i + 1]

#convert code in2 chars
    normal_string += chr(int(char_code))
#get 1st and 2nd for the 2 digit number
print("Og message: ", normal_string)
