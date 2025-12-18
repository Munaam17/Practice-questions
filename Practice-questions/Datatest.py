# from array import array


# test= "Hello world" 
# tuple1= (1,3,3,4)
# dict1= {'a':1, 'b':2, 'c':3}
# set1= {1,2,3,4,5, "a", "b"}
# print(type("1"))
# print(type(tuple1))
# print(type(dict1)) 
# print(type(set1))

# #typecasting is the process of converting a variable from one data type to another data type. In Python, you can perform typecasting using built-in functions such as int(), float(), str(), list(), tuple(), dict(), and set(). Here are some examples of typecasting in Python:
# # Converting a string to an integer
# str_num = "10"
# int_num = int(str_num)
# print(int_num)  # Output: 10        

# #converting an string to a float
# noob="5"
# float_=float(noob)
# print(float_)  # Output: 2.14
# print(type(float_))

# #tuple to list conversion
# tuple1= (10,2,3,4,5)
# list1= list(tuple1)
# print(list1)  # Output: [1, 2, 3, 4, 5]
# print(type(list1))  

# #simlarly you can convert list to tuple
# list2= [1,2,3,4,5]
# tuple2= tuple(list2)
# print(tuple2)  # Output: (1, 2, 3, 4, 5)
# print(type(tuple2))     


# #type casting is useful when you need to perform operations that require specific data types or when you want to ensure that your data is in the correct format for processing.
# #example of typecasting string to set
# str1= "hello"
# set2= set(str1)
# print(set2)  # Output: {'h', 'e', 'l', 'o'}
# print(type(set2))

# # eval is a built-in function in Python that evaluates a string expression and returns the result. It can be used to dynamically execute Python code represented as a string. Here's an example of how to use eval:
# # Example of using eval to evaluate a mathematical expression
# expr = "2 + 3 * 4"
# result = eval(expr)
# print(result)  # Output: 14
# print(type(expr), type(result))

# print(eval("10 + 20"))  # Output: 30
# print(eval("'Hello' + ' ' + 'World'"))  # Output: Hello World
# print(eval("[1, 2, 3] + [4, 5, 6]"))  # Output: [1, 2, 3, 4, 5, 6]

# # Note: Be cautious when using eval, especially with untrusted input, as it can execute arbitrary code and pose security risks.

# # Arrays in Python can be implemented using the built-in list data type or by using the array module for more efficient storage of homogeneous data types. Here's an example of how to create and manipulate arrays using both lists and the array module:
# # Using lists to create an array
# array_list = [1, 2, 3, 4, 5]
# print("Array using list:", array_list)  

# # Accessing elements
# print("First element:", array_list[0])  
# print("Last element:", array_list[-1])  
# print("Slice of array:", array_list[1:4])

# rans= range(10)
# print("Range object:", rans)
# print("Range as list:", list(rans))

# # why the range function is not working like array? becuase it is not an array it is a range object that generates a sequence of numbers on demand. To convert it to an array-like structure, you can use the list() function as shown above.
# list1=[1,'a', 3.5, True]
# print(list1)
# b=[]
# arra1= ["Alice", "Bob", "Charlie", "David"]
# for Ali in range(len(arra1)):
#     print(arra1[Ali])
#     b.append(arra1[Ali])
# print(b)
# print(len(b))
# stl= "Hello mister"
# print(len(stl))
# n=5
# for i in range(n,0,-1):
#     # print(i)
#     for j in range(1,i):
#         print(j, end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i):
#         print(j,end=' ')
#     print()

# for i in range(6,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=' ')
#     print()

# for i in range(1,6):
#     for j in range(6,0,-1):
#         print(j, end=' ')
#     print()

# 54321
# 5432
# 543
# 54
# 5
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j, end=' ')
#     print()


# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j, end=' ')
#     print()

# for i in range(6,0,-1):
#     for j in range(1,i):
#         print(j, end=' ')
#     print()

# for i in range(6,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i+2):
#         print(j, end=' ')
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i-1):
#         print(j, end=' ')
#     print()


# # 12345
# #  234
# #   3

# for i in range(1,6):
#     for j in range(1,i):
#         print(' ', end=' ')
#     for k in range(i,6):
#         print(k, end=' ')
#     print()