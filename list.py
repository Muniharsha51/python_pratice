# -------------------------Adding the numbers in list----------------

# list1 =[2,-5,44,5,54,10,33,99]
# sum=0
# #Method-1
# for i in list1:
#     sum+=i
# print(sum)

# #Method-2
# for i in range(0,len(list1)):
#     sum+=list1[i]
# print(sum)


#----------------------------printing even numbers in list------------
# list1 =[2,-5,44,5,54,10,33,99]
# for i in list1:
#     if i%2==0:
#         print(i)

# for i in range(0,len(list1)):
#     if i%2==0:
#         print(list1[i])


#----------------------------printing max, min number in list------------
# list2=[1,5,-5,22,85]
# max=list2[0]
# min=list2[0]
# #Method-1
# for i in list2:
#     if i >max:
#         max=i 
#     if i<min:
#         min=i
# print(max)
# print(min)


#---------------------------------------------------------------------------

# def prime_number(num):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#         if count ==2:
#             print('prime')
#         else:
#             print('not prime')

# prime_number(10)

#-------------------------------------------------------------------------------
# list1=[153,370,9474,154]

# num1=9474
# temp=num1
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit**len(str(num1))
#     temp=temp//10
# if sum==num1:
#     print('Armongstrong number')
# else:
#     print('Not Armongstrong number')

#----------------------------------------------------------------------
# def Armong_strong(input_num):
#     num1=input_num
#     temp=num1
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum+=digit**len(str(num1))
#         temp=temp//10
#     if sum==num1:
#         print(num1,'Armongstrong number')
#     else:
#         print(num1,'Not Armongstrong number')

# for i in list1:
#     Armong_strong(i)

#------------------------------------------Dupilicates--------------------------
# list1=[1,2,5,7,7,9,0,2,1]
# list2=[]
# for i in range(0,len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i]==list1[j]:
#             list2.append(list1[j])
# print(list2)



# ---------------------------------------Find Second Largest and Third Largest Element in list. ---------------------------

# list1=[10,12,54,41,30,5]
# sec_lar=list1[0]
# thi_lar=list1[0]
# list2=[]
# for i in range(0,len(list1)):
#     for j in range (i+1,len(list1)):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)
# print('second latgest number is ',list1[-2])
# print('third latgest number is ',list1[-3])


# ------------------------------------------------------------Reverse an Array. --------------------------------------------

# list1=[1,2,3,4,5,6,7,8,9]
# list2=[]
# #METHOD-1
# for i in range(len(list1),0,-1):
#     list2.append(i)
# print(list2)

#METHOD-2
# for i in list1:
#     list2.insert(0,i)
# print(list2)
# print(list1)

#METHOD-3

# low=0
# high=len(list1)-1
# while low<high:
#     list1[low],list1[high]=list1[high],list1[low]
#     low+=1
#     high-=1
# print(list1)

# -----------------------------------------------------Sorting an array----------------------------------------------------

# list1=[10,12,54,41,30,5]
# for i in range(0,len(list1)):
#     for j in range (i+1,len(list1)):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)

# -----------------------------arrange first half in ascending order and second half in descending order
# input: 8 7 1 6 5 9           output: 1 5 6 9 8 7

# list1=[8,7,1,6,5,9]
# list2=[]

#METHOD-1:

# for i in range(0,len(list1)):
#     for j in range (i+1,len(list1)):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)
# for i in range(0,len(list1)//2):
#     list2.append(list1[i])
# print(list2)
# for i in range(len(list1) - 1, len(list1) // 2 - 1, -1):
#     list2.append(list1[i])
# print(list2)


#METHOD-2
# low=len(list1)//2
# print(low)
# high=len(list1)-1
# print(high)
# while low<high:
#     list1[low],list1[high]=list1[high],list1[low]
#     low+=1
#     high-=1
# print(list1)

#1,5,6,7,8,9  1 5 6  9 8 7


#--------------------------------------------------finding or searching a nunmber (LINEAR SEARCH ALGORITHM)--------------------
# list1=[8,7,1,6,5,9]
# find=1
# for i in range(0,len(list1)):
#     if list1[i]==find:
#         print(i)
#         break

#METHOD-2
# flag=False
# for i in range(0,len(list1)):
#     if list1[i]==find:
#         flag=True
#         print(i)
#         break

# if flag==False:
#     print("Not found")\


#---------------------------------------METHOD-3
# def Linear_search(input_list,find_ele):
#     for i in range(0,len(input_list)):
#         if input_list[i]==find_ele:
#             return i
        
#     return 'not found'

# print(Linear_search(list1,find))




# Create a function that takes an array of strings and returns an array with only 
# the strings that have numbers in them. If there are no strings containing numbers, return an empty array.

# numInStr=(["1a", "a", "2b", "b"]) ➞ ["1a", "2b"]

# numInStr=(["abc", "abc10"]) ➞ ["abc10"]

# numInStr=(["abc", "ab10c", "a10bc", "bcd"]) ➞ ["ab10c", "a10bc"]

# numInStr=(["this is a test", "test1"]) ➞ ["test1"]

# list1=["1a", "a", "2b", "b"]   #OP: ['"1a","2b"]
# list2=[]
# for i in list1:
#     for j in i:
#         if j == char.isdigit():
#             print('true')




#-----------------------------------------------------------------------------------------------
# list1=[234,678,901,333]  #op: list2=[9,21,10,9]
# list2=[]



# def sum_of_digits(input_num):
#     sum = 0
#     while input_num > 0:
#         digit = input_num % 10
#         sum += digit
#         input_num =  input_num // 10 
#     return sum
        
# output_list = []
# list1 = [245, 678, 901, 333]
# for i in list1:
#     output_list.append(sum_of_digits(i))
# print(output_list)




#----------------------------------------------------Sorting problem

# list1=[20,15,26,2,98,6]
# new_list=[2,6,15,20,26,98]
# output=[]
# for i in list1:
#     output.append(new_list.index(i)+1)

# print(output)


# list1=[202,29,112,88]
# for i in list1:
#     print(i)

list1=[568,89,112,88,571]

def chec_inc_order(input_num):
    temp=input_num #568
    prev=10
    while temp>0:
        digit=temp%10 #8  6  5
        # print(digit)
        if digit >=prev:
            return False
        prev=digit #8   6    5
        temp=temp//10 #56   5  0
    return True

for i in list1:
    print (chec_inc_order(i))