# 9.Parse the following JSON to get all the values of a key ‘name’ within an array

# import json
# a=[ 
#    { 
#       "id":1,
#       "name":"name1",
#       "color":[ 
#          "red",
#          "green"
#       ]
#    },
#    { 
#       "id":2,
#       "name":"name2",
#       "color":[ 
#          "pink",
#          "yellow"
#       ]
#    }
# ]

# import json
# b=[]
# b=json.loads(a)
# dataList = [item.get('name') for item in b]
# print(dataList)
# # try:
# #     b=json.loads(a)
# # except Exception as e:
# #     print(e)
# #     for i in b:
# #        c=[item.get("name")]
# # print(c)

# # dataList = [item.get('name') for item in b]
# # print(dataList)


# def name(text):
#    a=text.split()
#    return a
# print(name("Ringphuliu bapei"))


# def greet(name):
#     return "Hello, " + name + " how are you doing today?"
# print(greet("Ningmei"))

# n = [3, 5, 7]

# def double(lst):
#     for x in lst:
#         x *= 2
#         print (x)
#     return lst

# print double(n)

# def a(n):
#     a=[]
#     for i in n:
#         i*= 2
#         a.append(i)
#     return a
# print(a([3, 5, 7]))

# PALINDROME:
# def ningmei(s): 
    # s=s.lower()
#  return s==s[::-1] 
# a="madam" 
# b=ningmei(a)
# print(b)
 
 
# a=[1,2,3,4,5]
# b=int(input("Enter the any number: "))
# d=[]
# c=[]
# for i in range(0,b):
#     c.append(a[i])
# print(c)

# Q Take the first N element

# a=[1,2,3,4,5]
# a=[]
# b=int(input("Enter the any number: "))
# d=[]
# i=0
# if len(a)<b:
#     print(a)
# elif len(a)==0:
#     print("[]")
# else:
#     while i<b:
#         d.append(a[i])
#         i+=1
#     print(d)

# a=[1,2,3]
# d=[]
# i=0
# while i<len(a):
#     c=a[-1]
#     b=c+1
#     d.append(b)
#     i+=1
# print(a,d)
# a=[1,2]
# b=[3,4]
# c=a+b
# print(c)

# def shortest(a):
#     c=a[-1]
#     b=c+1
#     return a+[b]
# print(shortest([1,2,3]))   





















