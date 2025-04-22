# Q.
#       * * * * *
#       * * * * *
#       * * * * *
#       * * * * *
#       * * * * *
#Methos-1
# num=5

# for i in range(0,num):
#     pattern=''
#     for j in range(0,num):
#         pattern+='* '
#     print(pattern,end=' ')
#     print('\n',end=' ')

#Method-2
# num=5
# for i in range(num):
#     for j in range(num):
#         print('*',end=' ')
#     print()

#--------------------------------------------------------------------------------------
# Q.
# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *
# num=5
# for i in range(num):
#     for j in range(num):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#--------------------------------------------------------------------------------------
# Q.
# *****
# *   *
# *   *
# *   *
# *****

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1 :
#             print('*', end='')
#         else:
#             print(' ',end='')
#     print()

#--------------------------------------------------------------------------------------
# Q.
# *****
# ** **
# * * *
# ** **
# *****

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1 :
#             print('*', end='')
#         else:
#             print(' ',end='')
#     print()

#--------------------------------------------------------------------------------------
# Q.

# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# num=5
# for i in range(num):
#     for j in range(num):
#         if i>=j:
#             print('*',end=' ')
        
#     print()
# for i in range(num-1):
#     for j in range(num-1):
#         if i<=j:
#             print('*',end=' ')
#     print()

#--------------------------------------------------------------------------------------

#      *
#     * *
#    * * *
#   * * * * 
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

#--------------------------------------------------------------------------------------
# Q.  G - ALFABET
# n=5
# mid=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or (i==mid and j>mid) or (j==n-1 and i>mid):
#             print('*', end='')
#         else:
#             print(' ',end='')
#     print()


# i+j=m-n
#--------------------------------------------------------------------------------------
# Q.
# 12345
# 12345
# 12345
# 12345
# 12345

# n=5
# for i in range(n):
#     start=1
#     for j in range(n):
#         print(start, end='')
#         start+=1
#     print()

#--------------------------------------------------------------------------------------
# Q.
# 1
# 12
# 123
# 1234
# 12345

# n=5
# for i in range(n+1):
#     start=1
#     for j in range(n):
#         if i>j :
#             print(start, end='')
#             start+=1
#     print()

#--------------------------------------------------------------------------------------
# Q. 
# 0
# 10
# 010
# 1010
# 01010

# n=5
# for i in range(n):
#     if i%2==0:
#         start=0
#     else:
#         start=1
#     for j in range(n):
#         if i>=j:
#             print(start, end='')
#             if start==0:
#                 start=1
#             else:
#                 start=0
#     print()

#--------------------------------------------------------------------------------------
# print(chr(97))
# print(chr(122))

# print(ord('A'))
# print(ord('['))

# n=4
# start=65
# for i in range(n):
#     for j in range(n):
#         if i >=j:
#             print(chr(start),end='')
#             start+=1
#     print()


