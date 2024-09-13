import random
import math

#an outer lop decrewase sin size each time
#the goal is to have the largest number at the end of th elist when the outer loop completes 1 cycle 
#the inner loop starts comparingf indexes at the beginning of the loop
#check if list[index] > list [Index + 1]
#if so, swap the iindex values
#when the innefr loop completes the largest number is at the end of the list

#decreemnt thr outer loop by 1

num_list = []

for i in range(5):
    num_list.append(random.randrange(1,10))

i = len(num_list ) - 1

while i > 1:
    j = 0

    while j < 1:
        if num_list[j] > num_list[ j + 1]:

            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = temp

        else:
            print()