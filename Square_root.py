# SQUARE ROOT


# def square(list):
#     i=0
#     b=[]
#     while i<len(list):
#         if list[i]==i**2:
#             b.append(i)
#         else:
#             b.append(list[i]*list[i])
#         i=i+1
#     return b
# list=[1,6,4,9,16,2,3]
# print(square(list))

# a="Navgurukul"
# print(a[1:-1])
 
 
# a="CodEWarS"
# i=0
# b=[]
# while i<len(a):
#     if a[i].isupper():
#         b.append(i)
#     i+=1
# print(b) 

# a=["Hello","World!","I","am","Ningmei"]
# print(" ".join(a))
# i=0
# while i<len(a):
#     if "," in a:
#         del a
#     else:
#         print(a[i],end=" ")
#     i+=1


# a="Hello!,WORLD"
# print(a.swapcase())
# i=0
# b=""
# while i<len(a):
#     if a[i].isupper():
#         b+=a[i].lower()
#     else:
#         b+=a[i].upper()
#     i+=1
# print(b)


# dic={"a":[1,2,3],"b":[4,5,6]}
# d={}
# a=[]
# for i in dic:
#     a1=[]
#     j=-1
#     while j>=-len(dic[i]):
#         b=dic[i][j]
#         a1.append(b)
#         j-=1
#     a.append(a1)
#     k=0
#     while k<len(a):
#         c=a[k]
#         k+=1
#     d[i]=c
# print(d)


# a="I came 1st and my friend came 5th"
# sum=0
# i=0
# while i<len(a):
#         if a[i].isnumeric():
#             sum+=int(a[i])
#         i+=1
# print(sum)
        
# a="I came 10 and my friend came 15"
# b=a.split()
# sum=0
# i=0
# while i<len(b):
#     if b[i].isnumeric():
#         sum+=int(b[i])
#     i+=1
# print(sum)


# a="Let me live unseen,unknown,unlamented when i die"
# count=0
# for i in a:
#     if i=="a"or i=="e" or i=="i" or i=="o" or i=="u":
#         count+=1
# print(count)
        
# list1=[10,20,30,40]
# list2=[100,200,300,400]
# for i ,j in zip (list1,list2):
#         print(i,j)
        
        
# for i in list1:
#     for j in list2:
#         print(i,j)

# list1=[10,20,[300,400,[5000,6000],500],30,40]
# list1[2][2].append(7000)
# print(list1)




# list1=["Hello","Take"]
# list2=["Dear","Sir"]
# c=[]
# for i in list1:
#     for j in list2:
#         b=i + j
#         c.append(b)
# print(c)


# a=[1,2,3],[4,5,6],[10,11,12],[7,8,9]
# i=0
# while i<len(a):
#     c=max(a)
#     i+=1
# print(c)


# Write a Python program to extract a list of values from a given list of dictionaries. Go to the editor
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Math
# [90, 89, 92]


marks = [{'Math': 90, 'Science': 92}, 
         {'Math': 89, 'Science': 94}, 
         {'Math': 92, 'Science': 88}]
b=input("Enter the subject:- ")

for i in marks:
    for j in i:
        if j==b:
            print(i[j])
            







