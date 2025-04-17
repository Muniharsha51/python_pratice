

#base condition- known values

#--------------------------------------EXAMPLE-1-----------------------------
# def fact(input)


#-------------------------------------EXAMPLE-2-----------------------------
# def print_nums(input_num):
#     if input_num ==0:
#         return
    
#     print(input_num)
#     print_nums(input_num-1)

# print_nums(5)

#-----------------------------EXAMPLE-3(Print natural numbers without for loop i.e., by  using recursion)-----------------------
# def print_nums(input_num):
#     if input_num ==0:
#         return
#     print_nums(input_num-1)
#     print(input_num)
    

# print_nums(5)

#-----------------------------EXAMPLE-4-----------------------------------------------------------------

# def print_nums(input_num):
#     if input_num ==0:
#         return
    
#     print(input_num)
#     print_nums(input_num-1)
#     print(input_num)
    

# print_nums(5)


#-----------------------------EXAMPLE-5(sum of digits)--------------------------------------------------
# # Function to calculate the sum of digits of a number using recursion
# def sum_of_digits(input_num):
#     # Base condition: if the number is 0, return 0
#     if input_num == 0:
#         return 0
    
#     # Recursive case: add the last digit to the sum of the remaining digits
#     return (input_num % 10 + sum_of_digits(input_num // 10))

# # Test the function with an example
# print(sum_of_digits(54321)) 

#------------------------------EXAMPLE-6(factorial)--------------------------------------------------
# def fact(input_num):
#     if input_num ==0 or input_num ==1:
#         return 1
#     return (input_num * fact(input_num-1))
# print(fact(5))
#------------------------------EXAMPLE-7(exponent)--------------------------------------------------
# def exponent(base,exp):
#     if exp==0:
#         return 1
#     return (base * exponent(base,exp-1))  ##2*2
#     # return (base *(base power exp-1))
# print(exponent(2,3))

#------------------------------EXAMPLE-8(reverse a string)--------------------------------------------------
# def reverse_string(input_str):
#     if len(input_str) == 0:
#         return input_str
#     return input_str[-1] + reverse_string(input_str[:-1])
# print(reverse_string("hello"))  


# #------------------------------EXAMPLE-8(reverse a string)--------------------------------------------------
# def reverse_string(input_str):
#     # Base condition: If the string is empty, return an empty string
#     if len(input_str) == 0:
#         return ""
    
#     # Debugging: Print the current state of the string and the last character being processed
#     print(f"Current string: {input_str}, Last character: {input_str[-1]}")
    
#     # Recursive case: Take the last character and add the result of reversing the rest of the string
#     # This line works by:
#     # 1. Taking the last character of the string using input_str[-1].
#     # 2. Recursively calling reverse_string on the rest of the string (input_str[:-1]).
#     # 3. Combining the last character with the reversed result of the remaining string.
#     return input_str[-1] + reverse_string(input_str[:-1])

# # Test the function with an example
# print(reverse_string("hello"))


# #------------------------------EXAMPLE-9(multipcation)--------------------------------  2*5 =2+2*4, 4+2*3 a+2*b-1
# def multi(a,b):
#     if a==0:
#         return 0
#     if b==0:
#         return 0

#     return a + multi(a,b-1)
# print(multi(11,5))

#--------------------------------EXAMPLE-10 (PALINDROME)------------------------------------------------
# def check_palindrome(input_str):
#     if len(input_str) <=1:
#         return True
    
#     return (input_str[0] == input_str[-1]) and check_palindrome(input_str[1:-1])
    
# print(check_palindrome("harsha"))

#--------------------------------EXAMPLE-10 (Maximum number in list)------------------------------------------------
# list1=[1,55,11,81,105]
# def max_num(list1):

#     if len(list1)==0:
#         return 'empty list'
#     if len(list1) ==1:
#         return list1[0]
    
#     res=max_num(list1[1:])
#     if list1[0] > res:
#         return list1[0]
#     else:
#         return res 
# print(max_num(list1))