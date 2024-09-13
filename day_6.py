import random
import math

rand_list = ["string", 1.234, 28]

one_to_ten = list(range(10))

rand_list = rand_list + one_to_ten
print(rand_list[0])
print("list length: ", len(rand_list))

first_three = rand_list[0:3]
for i in first_three:
    print("{} : {}".format(first_three.index(i), i))

print(first_three[0] * 3)

print("Index of string :", first_three.index("string"))
print("How many strings :", first_three.count("string"))

first_three[0] = "New Strting"
for i in first_three:
    print("{} : {}". format(first_three.index(i), i))

first_three.append("Another")
for i in first_three:
    print("{} : {}". format(first_three.index(i), i))