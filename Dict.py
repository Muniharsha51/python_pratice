



#Q.Given a list of words, return a dictionary where the keys are words and values are their lengths. -------------------------

# list1=["orange","apple","watermelon"]
# #op {"orange":6,"mango":5,"watermelon":10}

# res={}
# for i in list1:
#     res[i]=len(i)
# print(res)
#Q.Given two lists of equal length, create a dictionary where one list contains keys and the other contains values.------------

# list1=["orange","apple","watermelon"]
# list2=["v1","V2","V3"]

# res={}
# for i in range(len(list1)):
#     res[list1[i]] = list2[i]
# print(res)


#Q. Given a list of numbers, count the occurrences of each number and return a dictionary.-------------------------------------


# list1=[3,2,5,3,2,5,6,5,4,2]
# res={}
# for i in list1:
#     if i not in res:
#         res[i]=1
#     else:
#         res[i]=res[i]+1
# print(res)

#Q. Given a string, return a dictionary where keys are characters and values are their occurrence. ------------------------------

# str="hakuna matata"
# res={}
# for i in str:
#     if i not in res:
#         res[i]=1
#     else:
#         res[i]=res[i]+1
# print(res)

#Q.Swap keys and values of a dictionary. Store keys in a list. ------------------------------------------------------------------

# dict1={'h': 1, 'a': 5, 'k': 1, 'u': 1, 'n': 1, 'm': 1, 't': 2}
# dict2={}
#level-1

# for i,j in dict1.items():
#     dict2[j]=i

# print(dict2)

#Level-2

# for i,j in dict1.items():
#     if j not in dict2:
#         dict2[j]=[i]
#     else:
#         dict2[j].append(i)
# print(dict2)

#Q.Given a dictionary, find the key with the highest value. --------------------------------------------------------------------
# dict1={'k1':18,'k2':59,'k3':190,'k4':5}
# max_value=float('-inf')
# max_key='no key'
# for i,j in dict1.items():
#     if j>max_value:
#         max_value=j
#         max_key=i
# print(max_value) 
# print(max_key)

#Q. Given two dictionaries, merge them into one. If a key exists in both, sum their values. ------------------------------------
# dict1={'k1':15,'K2':25,'K3':10}
# dict2={'K3':90,'K4':1}

# res = {}
# for i, j in dict1.items():
#     res[i] = j
# for i,j in dict2.items():
#     if i in res:
#         res[i] = res[i] + j
#     else:
#         res[i] = j
# print(res)

#Q. #Anagrams - #STOP, POST, TOPS #AJAY, JAYA-----------------------------------------------------------------------------------