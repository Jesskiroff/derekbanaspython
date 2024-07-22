letter_z = "z"
num_3 ="3.14"
a_space = " "



def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False
    
#print("is Pi a float",isfloat(num_3))



def isint(str_val):
    try:
        int(str_val)
        return True
    except ValueError:
        return False
    
print("is pi an int",isint(num_3))