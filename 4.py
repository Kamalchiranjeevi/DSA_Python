#Q: 1 1 1 1
#   2 2 2 2
#   3 3 3 3
#   4 4 4 4
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(i, end = " ")
#     print()
#           or
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of cloumns: "))
# for i in range(1,r+1):
#     for j in range(c):
#         print(i, end=" ")
#     print()




# Q: 1 2 3 4 
#    1 2 3 4 
#    1 2 3 4
#    1 2 3 4
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of columns: "))
# for i in range(1,r+1):
#     for j in range(1,r+1):
#         print(j, end=" ")
#     print()
#               or
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of columns: "))
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         print(j, end=" ")
#     print()
    


# Q: 4 3 2 1 
#    4 3 2 1 
#    4 3 2 1 
#    4 3 2 1 
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of columns: "))
# for i in range(1,r+1):
#     for j in range(c,0,-1):
#         print(j, end=" ")
#     print()




# Q: 1 
#    1 2 
#    1 2 3 
#    1 2 3 4 
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
#                or
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of columns: "))
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()




# Q: 1 
#    2 3 
#    4 5 6 
#    7 8 9 10 
# num = int(input("Enter a number: "))
# a = 1
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(a, end=" ")
#         a += 1
#     print()
#               or
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of cloumns: "))
# a = 1
# for i in range(1, r+1):
#     for j in range(1,i+1):
#         print(a, end=" ")
#         a += 1
#     print()



# Q: 1 2 3 4
#    5 6 7
#    8 9
#    10
# num = int(input("Enter a number: "))
# a = 1
# for i in range(num,0,-1):
#     for j in range(1,i+1):
#         print(a, end=" ")
#         a += 1
#     print()
#               or
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of cloumns: "))
# a = 1
# for i in range(r,0,-1):
#     for j in range(1,i+1):
#         print(a, end=" ")
#         a += 1
#     print()



#Q: *
#   * *
#   * * *
#   * * * *
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of columns: "))
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print("*", end = " ")
#     print()


#Q:      *
#      * *
#    * * *
#  * * * *
# n = int(input())
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end = " ")
#     for k in range(i+1):
#         print("*", end = " ")
#     print()




#Q: * * * *
#     * * *
#       * *
#         *
# n = int(input())
# for i in range(1, n+1):
#     for k in range(i-1):
#         print(" ", end = " ")
#     for j in range(n-i):
#         print("*",end = " ")
#     print()




#Q:  * * * *
#    * * *
#    * *
#    *
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of columns: "))
# for i in range(1,r+1):
#     for j in range(c+1,i,-1):
#         print("*", end=" ")
#     print()



# Q: A 
#    A B 
#    A B C 
#    A B C D 
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(chr(ord('A') + (j-1)), end=" ")
#     print()



# Q: A 
#    B B 
#    C C C 
#    D D D D
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(chr(ord('A') + (i-1)), end=" ")
#     print()





# '''Q: Program that finds the prime numbers from x to y.'''
# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# prime = []
# for i in range(num1, num2+1):
#     if i > 1:
#         count = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             prime.append(i)
# print("the prime numbers from ",num1," to ",num2," are: ",prime)



# Q: * * * * * 
#    * * * * * 
#    * * * * * 
#    * * * * * 
#    * * * * * 
# r = int(input("Enter number of rows: "))
# c = int(input("Enter number of columns: "))
# for i in range(r):
#     for j in range(c):
#         print("*", end = " ")
#     print()


