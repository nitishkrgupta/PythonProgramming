# program to print different pattern

# 1. printing one *

print("*")
# *
print("----------------------------------")
# 2. printing two star vertically

print("*")
print("*")
print("----------------------------------")
# output
# *
# *

# 3. printing 4 * vertically 
for i in range(4):
    print("*")
print("----------------------------------")

# 5. Square / rectangle printing

# row = int(input("Enter no. of rows : "))
# col = int(input("Enter no. of columns : "))
# for i in range(row):
#     for j in range(col):
#         print("*", end=" ")
#     print()

# output
# * * * * 
# * * * * 
# * * * * 
# * * * *

# 6. printing square pattern with numbers
print("----------------------------------")
# row = int(input("Enter no. of rows : "))
# col = int(input("Enter no. of columns : "))
# val = 1
# for i in range(row):
#     for j in range(col):
#         print(val, end=" ")
#     print()

# output

# 1 1 1 1 
# 1 1 1 1 
# 1 1 1 1 
# 1 1 1 1 

# 7. 

# row = int(input("Enter no. of rows : "))
# col = int(input("Enter no. of columns : "))
# for i in range(row):
#     val = 1
#     for j in range(col):
#         print(val, end=" ")
#         val += 1
#     print()
    

# output

# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 

# 8. 

# row = int(input("Enter no. of rows : "))
# col = int(input("Enter no. of columns : "))
# val = 1
# for i in range(row):
#     for j in range(col):
#         print(val, end=" ")
#     print()
#     val += 1
#     if val > 9:
#         val = 1

# output

# 1 1 1 1 
# 2 2 2 2 
# 3 3 3 3 
# 4 4 4 4 

# 9. 

row = int(input("Enter no. of rows : "))
col = int(input("Enter no. of columns : "))

val = 1
for i in range(row):
    for j in range(col):
        print(val, end=" ")
        val += 1
        if val > 9: val = 1
    print()

# output

# 1 2 3 4 
# 5 6 7 8 
# 9 1 2 3 
# 4 5 6 7 