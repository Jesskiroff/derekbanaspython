#How tall is the pine tree? : 5

    #
   ###
  #####
 #######
#########
    #

#Use 1 while loop and 3 for loops
# 4 spaces :1 hash
# 3 spaces :3 hash
# 2 spaces :5 hash
# 1 spaces :7 hash
# 0 spaces :9 hash

#need to do
#1. decrement spacs by 1 each time through the loop
#2. Increment hashes by 2 each time through the loop
#3. save spaces to the stump by calculating tree height -1
#4. decrement from tree height until it eqauls 0
#5. prinnt spaces and then hasehs for each row
#6. print stump spaces and then 1 hash

#get num rows for tree
tree_height = input("How tall would you like to make the tree? ")

#convert into int
tree_height = int(tree_height)
#get the starting spaces for top of tree
spaces = tree_height -1 
#there is one hash to start that will be incremented
hashes = 1
# save stump spaces til later
stump_spaces = tree_height -1
# Make sure the right number of rows are printed
while tree_height != 0:
#print the spaces
    for i in range(spaces):
        print(" ", end ="")

#print the hashes
    for i in range(hashes):
        print('#', end ="")
#newline after each row is printed 
    print()
#That spaces is decremented by 1 each time
    spaces -= 1

#that hashes is incremented by 2 each time
    hashes+= 2
#decrement tree height each time to jump out of the loop
    tree_height -= 1
#print soces before stump and then before the hash
for i in range(stump_spaces):
    print(' ', end="")

print("#")