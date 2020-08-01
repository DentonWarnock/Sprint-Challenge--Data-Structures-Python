import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#
#
# O(n^2)
# original nested for loop runtime: 5.748511075973511 seconds
#
#

# BST is able to search and insert in O(log n) so should greatly speed up runtime from original O(n^2)
# create new BST instance and add all names from names_1 List
bst_1 = BSTNode("")

for name_1 in names_1:
    bst_1.insert(name_1) # O(log(n))
    
# check if name_1 contains name_2 - if so add name to duplicates list
for name_2 in names_2:
    if bst_1.contains(name_2): # O(log(n))
        duplicates.append(name_2)   
    

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

#
#
# O(log(n))
# BST runtime: 0.09202122688293457 seconds
#
#


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


start_time = time.time()

# list comprehension
duplicates = [name1 for name1 in names_1 if name1 in names_2]
#
#
# runtime: 1.0114490985870361 seconds
#
#

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

print("\n")

start_time = time.time()

# using python built in set data type
duplicates = set(names_1).intersection(set(names_2))
#
#
# runtime: 1.0114490985870361 seconds
#
#

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
