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
# start=1   # if we initial the start inside in a loop in pattern in every line numbers are start with 1
# for i in range(n+1):
    
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

# A
# BC
# DEF
# GHIJ

# n=4
# start=65
# for i in range(n):
#     for j in range(n):
#         if i >=j:
#             print(chr(start),end='')
#             start+=1
#     print()

#--------------------------------------------------------------------------------------

# Q.
#       * 
#      * * 
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
# * * * * * * *

# n=7
# for i in range(n):
#     for k in range(n-i-1):
#         print(" ", end='')

#     for j in range(n):
#         if i>=j:
#             print('*', end=' ')
#     print()

#--------------------------------------------------------------------------------------

# Q.
#       *
#      * *
#     *   *
#    *     *
#   *       *
#  *         *
# * * * * * * *
# n=7
# for i in range(n):
#     for k in range(n-i-1):
#         print(" ", end='')

#     for j in range(n):
#         if i==j or i==n-1 or j==0:
#             print('*', end=' ')
#         else:
#             print(" ",end=' ')
#     print()



#Q. -------------------------------------------Fibinocci---------------------------------

# 0 
# 1 1 
# 2 3 5
# 8 13 21 34
# 55 89 144 233 377
# 610 987 1597 2584 4181 6765
# 10946 17711 28657 46368 75025 121393 196418

# n=7 
# num1, num2=0,1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(num1,end=' ')
#             num1,num2=num2,num1+num2
#     print()

#--------------------------------------------------------------------------------------
# Q.
#             1 
#           2 1 0 
#         3 2 1 0 -1
#       4 3 2 1 0 -1 -2
#     5 4 3 2 1 0 -1 -2 -3
#   6 5 4 3 2 1 0 -1 -2 -3 -4
# 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5

# n=7
# for i in range(n):
#     start=i+1
#     for k in range(2*(n-i-1)):
#         print(' ', end='')
#     for j in range(2*i+1):
#         print(start, end=' ')
#         start-=1
#     print()

#--------------------------------------------------------------------------------------

#             1
#           2 1 2
#         3 2 1 2 3
#       4 3 2 1 2 3 4
#     5 4 3 2 1 2 3 4 5
#   6 5 4 3 2 1 2 3 4 5 6
# 7 6 5 4 3 2 1 2 3 4 5 6 7

# n=7
# for i in range(n):
#     track1=False
#     start=i+1
#     for k in range(2*(n-i-1)):
#         print(' ', end='')

#     for j in range(2*i+1):
#         print(start, end=' ')
#         if start==1:
#             track1=True

#         if track1== False:
#             start=start-1
#         else:
#             start+=1
#     print()

#--------------------------------------------------------------------------------------
#METHOD-2( HALF CODE ONLY)
# i=2
# str1=''
# for i in range(1,i+2):
#     str1=str1+str(i)+' '

# i=2
# for i in range (i,i+2):
#     str1=str(i)+' '+str1
# print(str1)

# FULL CODE FOR THE METHOD-2
# rows = 7
# result = ''

# for i in range(1, rows + 1):
#     str1 = ''
    
#     for j in range(i, 0, -1):
#         str1 += str(j) + ' '
    
#     for j in range(2, i + 1):
#         str1 += str(j) + ' '

#     spaces = '  ' * (rows - i)
#     result += spaces + str1.rstrip() + '\n'

# print(result)

