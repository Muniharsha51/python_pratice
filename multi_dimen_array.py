
mat1= [
    [2,5,4,9],
    [3,4,9,2],
    [5,1,9,2],
    [7,5,1,9]
]

# for i in range(len(mat1)):
#     for j in range(len(mat1[i])):
#         print(mat1[i][j], end=' ')
#     print()

#-------------------------------------Diagonal elements printing-----------------------------
# for i in range(len(mat1)):
#     for j in range(len(mat1[i])):
#         if i==j:
#             print(mat1[i][j], end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#-------------------------------------- lower  Diagonal elements printing----------------
# for i in range(len(mat1)):
#     for j in range(len(mat1[i])):
#         if i>j:
#             print(mat1[i][j], end=' ')
#     print()

#-------------------------------------- Two  Diagonal elements printing and sum of them----------------
# sum=0
# for i in range(len(mat1)):
#     for j in range(len(mat1[i])):
#         if i==j or i+j==len(mat1)-1:
#             sum+=j
#             print(mat1[i][j], end=' ')
            
#         else:
#             print(' ',end=' ')
#     print()
# print(sum)
#--------------------------------Boundry Elements-------------------------
# n=len(mat1)
# for i in range(len(mat1)):
#     for j in range(len(mat1[i])):
#         if i==0 or j==0 or i== n-1 or j==n-1:
#             print(mat1[i][j], end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#---------------------------Adding of matrix-------------------------------------
# mat1= [
#     [2,5,4,9],
#     [3,4,9,2],
#     [5,1,9,2],
#     [7,5,1,9]
# ]

# mat2=[
#     [5,1,9,2],
#     [7,5,1,9],
#     [2,5,4,9],
#     [3,4,9,2]
# ]

#METHOD-1
# for i in range(len(mat1)):
#     for j in range(len(mat1[i])):
#         print(mat1[i][j]+mat2[i][j], end=' ')
#     print()

#METHOD-2
# mat3=[]
# for i in range(len(mat1)):
#     mat3.append([])
#     for j in range(len(mat1[i])):
#         # print(mat1[i][j]+mat2[i][j], end=' ')
#         mat3[-1].append(mat1[i][j]+mat2[i][j])
#     print()
# print(mat3)


#---------------------------transpose of a matrix-------------------------------------

mat1= [
    [2,5,4,9],
    [3,4,9,2],
    [5,1,9,2],
    [7,5,1,9]
]


# op: 
# mat1=[
#     [2,3,5,7],
#     [5,4,1,5],
#     [4,9,9,1],
#     [9,2,2,9]
# ]

#METHOD-1:

# #METHOS-2
# mat2= [
#     [2,5,4,9],
#     [3,4,9,2],
#     [5,1,9,2],
#     [7,5,1,9]
# ]

# for i in range(len(mat1)):
#     for j in range(len(mat1[i])):
#         [mat1[i][j]]=[mat2[j][i]]
#         # [mat1[i][j], mat2[j][i]] = [mat2[j][i], mat1[i][j]]
# print(mat1)