import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
        
#         # check if tree contains values
#             # if not 
#                 # insert value
#                 # becomes root
#             # if so:
#         if sorted(value) > sorted(self.value) and self.right == None:
#             self.right = BinarySearchTree(value)
            
#         elif sorted(value) < sorted(self.value) and self.left == None:
#             self.left = BinarySearchTree(value)
            

#         elif sorted(value) > sorted(self.value) and self.right != None:
#             self.right.insert(value)
#         elif sorted(value) < sorted(self.value) and self.left != None:
#             self.left.insert(value)
                    

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         if self.value == target:
#             return True
#         elif self.right == None and self.left == None:
#             return False
        
#         elif sorted(target) > sorted(self.value) and self.right != None:
#             self = self.right
#             return self.contains(target)
#         elif sorted(target) > sorted(self.value) and self.right == None:
#             return False

#         elif sorted(target) < sorted(self.value) and self.left != None:
#             self = self.left
#             return self.contains(target)
#         elif sorted(target) < sorted(self.value) and self.left == None:
#             return False
# bst = BinarySearchTree(names_1[11])        
# # for name_1 in names_1:  Runtime complexity is O(n ^ 2)
# #     for name_2 in names_2:
# #         if name_1 == name_2:
# #             duplicates.append(name_1)
# for name_1 in names_1:
#     bst.insert(name_1)
# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#-- stretch for python collections only --
# name_store = [i for i in names_1]
# duplicates = [i for i in names_2 if i in names_1]

# # def b_search(target, arr):
# #     mid = len(arr) // 2
# #     print(target)
# #     if target == arr[mid] or target == arr[0]:
# #         duplicates.append(target)
# #         return True
# #     elif sorted(target) < sorted(arr[-1]) or sorted(target) > sorted(arr[0]):
# #         return False
# #     elif sorted(target) < sorted(arr[mid]):
# #         return b_search(target, arr[:mid])
# #     elif sorted(target) > sorted(arr[mid]):
# #         return b_search(target, arr[mid:])


# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")
