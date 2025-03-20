#---------------------------------------------- EASSY LEVEL PROBLEMS

# Q-1.write a program to check if a given number is positive, negative, or zero. 

num=-1
if num>0:
    print('positive number')
else:
    if num==0:
        print('zero is not a posive or negative number')
    
    else:
        print('negative number')



# Q-2.Determine if a number is odd or even. 

num1=55
if num1%2==0:
    print('it is even number')
else:
    print('it is an odd number')


# Q-3.Check if a person is eligible to vote (age >= 18).

age=16
if age>18:
    print('person is eligible for voting')
else:
    print('person is not eligible for voting')


# Q-4. Write a program to find the greatest of two numbers. 

num2=5
num3=11
if num2>num3:
    print('num2 is greatest number')
else:
    print('num3 is greatest number')


# Q-5. Print "Pass" if a student scores more than 40 marks otherwise, print "Fail."

marks=5
if marks>40:
    print('pass')
else:
    print('Fail')


# Q-6.Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.). 

day=1
if day==1:
    print('Monday')
elif day==2:
    print('Tuesday')
elif day==3:
    print('Wednesday')
elif day==4:
    print('Thuresday')
elif day==5:
    print('Friday')
elif day==6:
    print('Saturday')
elif day==7:
    print('Sunday')
else:
    print('Enter 1-7 only')

# Q-7.Implement a simple calculator to perform addition, subtraction, multiplication, and division.

# number1 = float(input("Enter first number: "))
# number2 = float(input("Enter second number: "))
# operator= input('enter +,-,*,/ any onething')

# if operator == '+':
#     result = number1 + number2
# elif operator == '-':
#     result = number1 - number2
# elif operator == '*':
#     result = number1 * number2
# elif operator == '/':
#     if number2 != 0:
#         result = number1 / number2
#     else:
#         result = "Error: Division by zero"
# else:
#     result = "Error: Invalid operator"

# print("Result:", result)

# Q-8.Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).

# num4=int(input("Enter the number if the month : "))
# if num4==1:
#     print('January')
# elif num4==2:
#     print('february')
# elif num4==3:
#     print('March')
# elif num4==4:
#     print('April')
# elif num4==5:
#     print('May')
# elif num4==6:
#     print('June')
# elif num4==7:
#     print('July')
# elif num4==8:
#     print('Augest')
# elif num4==9:
#     print('September')
# elif num4==10:
#     print('October')
# elif num4==11:
#     print('November')
# elif num4==12:
#     print('December')
# else:
#     print('Enter the valid number')

#---------------------------------------------- MEDIUM LEVEL PROBLEMS

# Q-1.Write a program to find the greatest of three numbers. 2 5 1

# first=int(input('Enter the first number : '))
# second=int(input('Enterr the second number : '))
# third=int(input('Enter the third number : '))

# if first>second and first>third:
#     print('First number is greatest number')
# elif second>first and second>third:
#     print('second number is geatest number')
# elif third>first and third>second:
#     print('third number is greatest number')
# else:
#     print('enter valid numbers')



# Q-2.Check if a year is a leap year. 

# z=int(input("Enter the year : "))
# if z % 4 == 0 and z % 100 != 0:
#     print("is is a leaf year")
# else:
#     print('it is not a leaf year')




# Q-3.Write a program to classify a character entered by the user as a vowel, consonant, or neither. 

# text=input('Enter the character : ')
# if text=='a' or text=='e' or text=='i' or text=='o' or text=='u' :
#     print('it is an vowel')
# elif text.isdigit():
#     print('it is an number')
# else:
#     print('it is an consonent')




# Q-4.Calculate the grade of a student based on the marks they 
# score: 
# 1.  90-100  : Grade A 
# 2.  80-89  : Grade B 
# 3.  70-79  : Grade C 
# 4.  <70  : Fail. 



grade=50


if grade >=90:
    print("Grade A")
elif grade>=89:
    print('Grade B')
elif grade>=79:
    print('Grade C')
elif grade<70:
    print("Fail")
else:
    print("enter the valid grade")
    




