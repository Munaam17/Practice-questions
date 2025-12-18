# # Armstrong number

# # Number=22
# # how many values=2
# # Sum of square stored=2^2 + 2^2 
# # if sum of square stored == Number:
# #     print("Armstrong number")
# # else:
# #     print("Not an Armstrong number")

# for i in range(1000):
#     num = i       
#     result = 0
#     n = len(str(num)) 
#     while i !=0:
#         digit = i % 10
#         result = result + digit ** n
#         i = i // 10
#     if result == num:
#         print(f"{num} is an Armstrong number")
    

# Pyhton patterns program

# n = int(input("Enter no of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()


# n = int(input("Enter no of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i, end=' ')
#     print()

# n = int(input("Enter no of rows: "))
# for i in range(n):  
#     for j in range(n):
#         if i == j or j == 0 or i == n-1:
#             print('*', end='')
#         else:
#             print(end=' ')
#     print()

# factorial program using recursion

# n = int(input("Enter number here to know the Factorial: "))
# def factorial(n): 
#     if n == 0:  # base case
#         return 1 
#     else: 
#         return n * factorial(n-1) #recursion function
# print(f"The Factorial of {n} is {factorial(n)}")    

# factorial program using loop

# Number = int(input("Enter number here to know the Factorial: "))
# factorial = 1
# for i in range(Number, 0, -1):
#     factorial = factorial * i  #f=1*5= 5, f = 5*4=20, f=20*3=60, f=60*2=120, f=120*1=120
#     print(factorial)
# print(f"The Factorial of {Number} is {factorial}")



# star pattern

# number = int(input("Enter number of rows: "))
# for i in range(number):
#     for j in range(number):
#         if i == 0 or j == number - 1 or i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# # number pattern
# n = int(input("Enter number of rows: "))
# a = 1
# for i in range(n+1):
#     for j in range(i):
#             print(format(a, ">4"), end=' ')
#             a += 1
#     print()

# string pattern

# string = input("Enter a string: ")
# length = len(string)
# for i in range(length): 
#     for j in range(i+1): 
#         print(string[j], end=' ')
#     print()

# Fabonacci series
# n = int(input("Enter number of terms: "))
# a, b = 0, 1
# for i in range(n): 
#     print(a, end=' ')
#     temp = a   
#     a = b            
#     b = temp + b  

# printing number in right angle triangle
# n = int(input("Enter number of rows: ")) #4
# for i in range(n,0,-1): #4, 3, 2, 1
#     for j in range(1,i+1): #1--4+1, 1--3+1, 1--2+1, 1--1+1
#         print(j, end=' ')  #1 2 3 4, 1 2 3, 1 2, 1
#     print()

    
# number = int(input("Enter number of rows: "))
# for i in range( number, 0, -1):
#     for j in range(1, i+1):
#         print(i, end=' ')
#     print()

# prime number

# num = int(input("Enter a number: "))
# if num <= 1:
#     print(f"{num} is not a prime number")
# else:
#     for i in range(num-1, 1, -1):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             break 
#     else:
#         print(f"{num} is a prime number")

# Prime numbers in a given range

# upper = int(input("Enter upper limit: "))# 8
# lower = int(input("Enter lower limit: "))# 5
# for i in range(lower, upper+1):# 5--9, 6--9, 7--9, 8--9, 
#     if i > 1: #5>1 Y 6>1 Y 7>1 Y 8>1 Y
#         for j in range(2, i):# 2--5, 2--6, 2--7, 2--8
#             if i % j == 0:  #5%2==0 N, 5%3==0 N, 5%4==0 N, 6%2==0 Y, 7%2==0 N, 7%3==0 N, 7%4==0 N, 7%5==0 N, 7%6==0 N, 8%2==0 Y
#                 break
#         else:
#             print(i)   


# # Star pattern program
# n= int(input("Enter no of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if i==n or i+j==n+1 or j-i==n-1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# n= int(input("Enter no of rows: "))
# k= 2
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if i+j==n+1 or j-i==n-1:
#             print('*', end='')
#         elif i==n and j!=k:
#             print('*', end='')
#             k+=2
#         else:
#             print(' ', end='')
#     print()


# for perfect no

# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     if (n%i)==0:
#         sum=sum+i #12/2
# sum=sum/2
# if sum==n:
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number") 


# # perfect no intervals

# lower=int(input("Enter lower limit: "))
# upper=int(input("Enter upper limit: "))
# for i in range(lower, upper+1):
#     sum=0
#     for j in range(1,i):
#         if (i%j)==0: 
#             sum=sum+j 
#     if sum==i:
#         print(f"{i} is a perfect number")  

# Swapping two numbers without using third variable
# 1st using 3rd variable

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(f"Before swapping: a = {a}, b = {b}")
# temp = a
# a = b
# b = temp
# print(f"After swapping: a = {a}, b = {b}")


# # 2nd without using 3rd variable
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(f"Before swapping: a = {a}, b = {b}")
# a = a + b  # a=5+10=15
# b = a - b  # b=15-10=5
# a= a - b  # a=15-5=10
# print(f"After swapping: a = {a}, b = {b}")

# 3rd using multiplication and division
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(f"Before swapping: a = {a}, b = {b}")
# a = a * b  # a=5*10=50
# b = a // b  # b=50//10=5                    
# a = a // b  # a=50//5=10
# print(f"After swapping: a = {a}, b = {b}")

# # 4th using bitwise XOR operator
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(f"Before swapping: a = {a}, b = {b}")
# a = a ^ b  # a=5^10
# b = a ^ b  # b=(5^10)^10=5
# a = a ^ b  # a=(5^10)^5=10
# print(f"After swapping: a = {a}, b = {b}")      

# 5th using tuple unpacking
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))         
# print(f"Before swapping: a = {a}, b = {b}")
# a, b = b, a
# print(f"After swapping: a = {a}, b = {b}")      

# 6th using list unpacking
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))         
# print(f"Before swapping: a = {a}, b = {b}")     
# a, b = [b, a]
# print(f"After swapping: a = {a}, b = {b}")    
# 
# 
# *
# **
# ***
# ****          

# n = int(input("Enter number of rows: "))
# for i in range(n): #(0,4) 0,1,2,3
#     for j in range(i+1):# 0,1,2
#         print('*', end='')
#     print() 


# using while loop

# *
# **
# ***
# ****
# i=0
# while i<n: #50<4y, 0<4y
#     j=i+1  #0+1=1, 1+1=2, 2+1=3, 3+1=4
#     while j>0:  #1>0y, 2>0y, 3>0y, 4>0y
#         print('*', end='')
#         j=j-1
#     print()
#     i=i+1

# Star pattern equilateral triangle using while loop

#    * 
#   * *
#  * * *
# * * * *   

# number =int(input("Enter no of rows: "))

# row = 0
# while row < number: #0<4, 1<4, 2<4, 3<4 Y 4<4 N
#     space = number - row - 1  #4-0-1=3, 4-1-1=2, 4-1-1=1, 4-3-1=0
#     while space > 0: #3>0, 2>0, 1>0 Y 0>0 N
#         print(end=' ') #___
#         space = space -1 #3-1=2, 2-1=1, 1-1=0
#     star = row + 1 #0+1=1, 1+1=2, 2+1=3, 3+1=4
#     while star > 0: #1>0, 0>0 N
#         print("*", end=" ") #*_
#         star = star - 1  #1-1=0
#     row = row + 1 #0+1=1
#     print() #next line

#  *
# *  *
#*    *
# *  *
#  *

# for i in range(5): #0,1,2,3,4 5-->7 2, 111, 3, 9, 7-->9, 111, 12, 9-->11, 111, 15
#     for j in range(5): #0,1,2,3,4
#         if i+j==2 or j-i==2 or i-j==2 or i+j==6: #0+2, 1+1, 2+1 (i+j==2) 3-1, 4-2(j-i==2), 3-1,4-2 (i-j==2), 3+3=6 (i+j==6)
#             print("*", end="") #(0)  *   (1) *  *  (2)*    * (3) * * (4)  *  
#         else:
#             print(" ",end= "") #(0)__ __ (1)_  _  _ (2) ___ (3)_ _ _ (4)__ __
#     print()

# Reverse a string

# n = input("Enter the word you wanted to reverse: ")
# a = " "
# for i in n:
#     a = i + a
# print (a)

# with function to reverse a string

# def reverse(sting1): 
#     reversed_string = ' '
#     for i in sting1:
#         reversed_string = i + reversed_string
#     print(f"here is your reversed word: {reversed_string}")


# sting1 = input("Enter the word you wanted to reverse: ")
# print(f"Here is the word you wanted a reverse for: {sting1}")
# reverse(sting1)

# Square pattern number program
# 1 2 3
# 8 9 4
# 7 6 5

#Here we'll use nested list or multi dimensional array's
# fg=3
# ar=[0]
# for x in range(fg):
#     print(ar, end = "",)
# print()

# ar_l = [[0 for x in range(fg)] for y in range(fg)]
# print(ar_l, x)


# num = int(input("Enter no of rows: "))
# n_list = [[0 for x in range(num)]  for y in range(num)]
# n = 1
# low = 0
# high = num - 1
# count = int((num+1)/2)

# for i in range(count):
#     for j in range(low,high+1):
#         n_list[i][j] = n
#         n = n+1
#     for j in range(low+1,high+1):
#         n_list[j][high]= n
#         n = n+1
#     for j in range(high-1,low-1,-1): #2-1=1, 0-1=-1
#         n_list[high][j]= n 
#         n = n+1
#     for j in range(high-1,low,-1):
#         n_list[j][low]= n
#         n = n+1
#     low = low+1
#     high = high-1


# for i in range(num): #0,1,2,3,4
#     for j in range(num):  #0
#         print(n_list[i][j], end = '\t')  
#     print()
    
# print ()
# for j in range (1,-4,-1):  #reversing a loop we should keep in mind starting val should be greater than stopping val
#     print(j, end=' ')
# print()

# GCD of 2 numbers

# n1 = int(input("Enter the 1st number for GCD: "))
# n2 = int(input("Enter the 1st number for GCD: "))


# a = []
# b = []
# c = []

# for no1 in range(1,n1+1):
#     if n1%no1 == 0:
#         a.append(no1)
# for no2 in range(1,n2+1):
#     if n2%no2 == 0:
#         b.append(no2)

# for val in a:
#     if val in b:
#         c.append(val)
        
# # for printing
# if len(c) > 0:
#     print(f"Here are the Common Divisors:{c}")
#     print(f"Here is the Greatest Common Divisor:{c[-1]}")
# else:
#     print("No common divisor")


# import math 
# print(math.gcd(50,45))


# # GCD with recurssion

# def imputeGCD(a,b):
#     if b == 0:
#         return a 
#     else: 
#         return imputeGCD(b,a%b)
    

# a = int(input("Enter the 1st number for GCD: "))
# b = int(input("Enter the 2nd number for GCD: "))

# print(imputeGCD(a,b))

# num = int(input("Enter no of rows: "))

# For rows
# for row in range(1, num+1):
#     # For spaces | row increases spaces decrease row - i +1
#     for sp in range(1, num - row +1): #1-3-1+1=3 (1,3) 1,2
#         print(format(" ",'>3'),end="")
#     # For numbers on left side
#     for ln in range(row, 0, -1): #(1,0,-1) -1 to reverse the loop
#         print(format(ln,">3"), end="")
#     # For numbers on left side
#     for rn in range(2, row + 1): # 2,1+1=2 (2,2) not execute on 1st run
#         print(format(rn,">3"), end="") 
#     print ()

#pyramid number pattern

# n = 1
# for row in range(num):
#     # For spaces | row increases spaces decrease row - i +1
#     for sp in range(num - row +1): #1-3-1+1=3 (1,3) 1,2
#         print(format(" ",">3"), end="")
#     # For numbers on left side
#     for str in range(row + 1): # 2,1+1=2 (2,2) not execute on 1st run
#         print(format(n,">6"), end="") 
#         n+=1
#     print ()


# # Guess the output

# x = False
# if x:
#     print(x, True)
# else:
#     print(x, False)


# #
# a = ["3,2,3,4",8]
# for i in range(len(a)):
#     print(a[i])

# print()

# for i in a:
#     print(a) #printing the element present in th list
#     print(a[-1])



# n=3
# b=1
# for i in range(0,n):
#     for j in range(n-i+1):  #space= n-i 3-1=2, 3-2=1, 3-3=0
#         print(end=" ")
#     for j in range(i+1):    #i=1 (0,1), 2(0,2)) 0+1=1, 1-3-1=2
#         print(b, end= " ")
#         b+=1
#     print()


# Selection Sort Algorithm

#1- Consider 0th index as min val
#2- Now compare that min val in list and if found then min val is that number is list after it traverse the whole list and found the min val.
#3- Swap the min val index with 0th index postion number 
#4- And Repeat

# lista[0], lista[min_ind] = lista[min_ind], lista[0] #swapping
# print(lista[0])
# or can use do using 3rd variable

# temp = lista[min_ind] #4 - 1
# lista[min_ind] = lista[0]  #0 - 56
# lista[0] = temp #1
# print(lista[0])


# sort_it = sorted(lista)
# print(min_val)
# print(min_ind)
# print(sort_it)

# for sorting in ascending order using Selection Sort Algo

# num = int(input("How many numbers you want in a list?: "))
# lista = [int(input(f"Enter number {x} in your list: ")) for x in range(1,num+1)]
# print("Unsorted list", lista)

# for i in range(len(lista)-1):
#     m_ind = i
#     for j in range(i+1,len(lista)):
#         if lista[j] < lista[m_ind]:
#             m_ind = j
#     if lista[i] != lista[m_ind]:
#         lista[i], lista[m_ind] = lista[m_ind], lista[i]

# print(lista)

# # for sorting in descending order using Selection Sort Algo
 
# num = int(input("How many numbers you want in a list?: "))
# # lista = [int(input(f"Enter number {x} in your list: ")) for x in range(1,num+1)]
# lista = []
# for i in range(1, num+1):
#     lista.append(int(input(f"Enter the {i} in your list: ")))


# print("Unsorted list", lista)

# for i in range(len(lista)-1):
#     m_ind = i
#     for j in range(i+1,len(lista)):
#         if lista[j] > lista[m_ind]:
#             m_ind = j
#     if lista[i] != lista[m_ind]:
#         lista[i], lista[m_ind] = lista[m_ind], lista[i]

# print(lista)

# Selection sort Algo Using built-in python function such as min() & index() 

# for i in range(len(lista)-1):
#     min_val = (min(lista[i: ])) #when i=0 from 0th index, when i=1 consider min val from index 1 onwards for minimum in the list
#     min_ind = lista.index(min_val, i) #here i to start finding minimum from ith index onward not backward
#     print(min_val , min_ind)
#     if lista[i] != lista[min_ind]:
#         lista[i], lista[min_ind] = lista[min_ind], lista[i] #12, 12 = 12, 12
#     print(lista)
# print(f"final sorted list {lista}")

# Bubble Sort Algo

# lista = [10,90,9,0,0,1,2]

# print("Unsorted list", lista)
# print()

# for i in range(len(lista)-1): #4
#     count = len(lista)-i-1
#     for j in range(count): #4
#         if lista[j] > lista[j+1]:  #1>4
#             lista[j], lista[j+1] = lista[j+1], lista[j]  #4, 0 = 0, 4
#             print(lista)
#         else:
#             print(lista)
#     print()

# print("Sorted list", lista)




# Palindrome or not

# stringa = input("enter string you need to know is palindrome or not: ")
# # int(stringa)
# reversed_stringa = " "
# for i in range(len(stringa)-1,-1,-1):
#     reversed_stringa = reversed_stringa + stringa[i] 
#     # print()
# print(reversed_stringa)


# # Slicing
# rev_s = stringa [::-1]
# # print(rev_s)
# if stringa == rev_s:
#     print(f"{stringa} is Palindrome")
# else:
#     print(f"{stringa} is not Palindrome")


# Sum of digits of postive intergers


# num = int(input("Enter the postive integer number you want the sum of digits for: "))

# using For loop 

# b = str(num)
# result = 0
# # print(len(b))
# for i in range (len(b)):
#     a = num % 10
#     result = result + a
#     num = num // 10

# print(result)


# using while Loop

# while num > 0:
#     a = num % 10
#     result += a
#     num = num // 10

# print(result)


# indexing in nested list using slicing 

# a = ["these", "are", "used", 12, [12, "56qweqe", " r"], '2', "k"]
# print(a[1:5][0:4][3][1][5:-3:-1])
# print(a[4:5][0][2])
# print(a[4::-1][0][1][1])

# Quick Sort Algorithm Ascending order with 1st element as pivot


# def pivot_place(list1, first, last):
#     pivot = list1[first]
#     left = first + 1
#     right = last
#     while True:    #if cond 2 and 3 fails we will swap val of left and right and check or start once again where it was on, so this loop is for that purpose
#         while left <= right and list1[left] <= pivot:
#             left = left + 1
#         while left <= right and list1[right] >= pivot:
#             right = right - 1
#         if right < left:   #swap pivot with right when pivot is first and also when cond 1 fails
#             break          #now to avoid the while True loop to be infintie we have break out of the loop and swap val of pivot 
#         else:              #swap left and right when cond 2 and 3 fails
#             list1[left], list1[right] = list1[right], list1[left]
#     list1[first], list1[right] = list1[right], list1[first]   #swapping pivot with right, and coming out of the function because pivot reach the correct position now have to divide and conquer
#     return right         #here returning the pivot val

# def quicksort(list1, first, last):
#     if first < last:    #run until this cond is true, because we want it to run until and unless first == last
#         p = pivot_place(list1, first, last)
#         quicksort(list1, first, p-1)  #for left side of pivot val, it divides and sort and goes on
#         quicksort(list1, p+1, last)   #for right side of pivot val, it divides and sort and goes on

# #input
# list1 = [100,45,1,25,101,0,99,7,4,23]
# n = len(list1)
# quicksort(list1, 0, n -1)

# print(list1)


# # Quick Sort Algorithm Descending order with 1st element as pivot


# def pivot_place(list1, first, last):
#     pivot = list1[first]
#     left = first + 1
#     right = last
#     while True:    #if cond 2 and 3 fails we will swap val of left and right and check or start once again where it was on, so this loop is for that purpose
#         while left <= right and list1[left] >= pivot:
#             left = left + 1
#         while left <= right and list1[right] <= pivot:
#             right = right - 1
#         if right < left:   #swap pivot with right when pivot is first and also when cond 1 fails
#             break          #now to avoid the while True loop to be infintie we have break out of the loop and swap val of pivot 
#         else:              #swap left and right when cond 2 and 3 fails
#             list1[left], list1[right] = list1[right], list1[left]
#     list1[first], list1[right] = list1[right], list1[first]   #swapping pivot with right, and coming out of the function because pivot reach the correct position now have to divide and conquer
#     return right         #here returning the pivot val

# def quicksort(list1, first, last):
#     if first < last:    #run until this cond is true, because we want it to run until and unless first == last
#         p = pivot_place(list1, first, last)
#         quicksort(list1, first, p-1)  #for left side of pivot val, it divides and sort and goes on
#         quicksort(list1, p+1, last)   #for right side of pivot val, it divides and sort and goes on

# #input
# list1 = [100,45,1,25,101,0,99,7,4,23]
# n = len(list1)
# quicksort(list1, 0, n -1)
# print(list1)


# # Quick Sort Algorithm Descending order with last element as pivot

# def pivot_place(list1, first, last):
#     pivot = list1[last]
#     left = first
#     right = last - 1
#     while True:    #if cond 2 and 3 fails we will swap val of left and right and check or start once again where it was on, so this loop is for that purpose
#         while left <= right and list1[left] >= pivot:
#             left = left + 1
#         while left <= right and list1[right] <= pivot:
#             right = right - 1
#         if right < left:   #swap pivot with left when pivot is last and also when cond 1 fails
#             break          #now to avoid the while True loop to be infintie we have break out of the loop and swap val of pivot 
#         else:              #swap left and right when cond 2 and 3 fails
#             list1[left], list1[right] = list1[right], list1[left]
#     list1[last], list1[left] = list1[left], list1[last]   #swapping pivot with left, and coming out of the function because pivot reach the correct position now have to divide and conquer
#     return left         #here returning the pivot val

# def quicksort(list1, first, last):
#     if first < last:    #run until this cond is true, because we want it to run until and unless first == last
#         p = pivot_place(list1, first, last)
#         quicksort(list1, first, p-1)  #for left side of pivot val, it divides and sort and goes on
#         quicksort(list1, p+1, last)   #for right side of pivot val, it divides and sort and goes on

# #input
# list1 = [100,45,1,25,101,0,99,7,4,23]
# n = len(list1)
# quicksort(list1, 0, n -1)
# print(list1)


# # Quick Sort Algorithm Ascending order with last element as pivot

# def pivot_place(list1, first, last):
#     pivot = list1[last]
#     left = first
#     right = last - 1
#     while True:    #if cond 2 and 3 fails we will swap val of left and right and check or start once again where it was on, so this loop is for that purpose
#         while left <= right and list1[left] <= pivot:
#             left = left + 1
#         while left <= right and list1[right] >= pivot:
#             right = right - 1
#         if right < left:   #swap pivot with left when pivot is last and also when cond 1 fails
#             break          #now to avoid the while True loop to be infintie we have break out of the loop and swap val of pivot 
#         else:              #swap left and right when cond 2 and 3 fails
#             list1[left], list1[right] = list1[right], list1[left]
#     list1[last], list1[left] = list1[left], list1[last]   #swapping pivot with left, and coming out of the function because pivot reach the correct position now have to divide and conquer
#     return left         #here returning the pivot val

# def quicksort(list1, first, last):
#     if first < last:    #run until this cond is true, because we want it to run until and unless first == last
#         p = pivot_place(list1, first, last)
#         quicksort(list1, first, p-1)  #for left side of pivot val, it divides and sort and goes on
#         quicksort(list1, p+1, last)   #for right side of pivot val, it divides and sort and goes on

# #input
# list1 = [6,5,4,3,2,1,1,1,0]
# n = len(list1)
# quicksort(list1, 0, n -1)
# print(list1)


# # With random as pivot and then last
# import random   
# import statistics
# def pivot_place(list1, first, last):
#     r_index = random.randint(first, last)
#     list1[last], list1[r_index] = list1[r_index], list1[last]
#     pivot = list1[last]
#     left = first
#     right = last - 1
#     while True:    #if cond 2 and 3 fails we will swap val of left and right and check or start once again where it was on, so this loop is for that purpose
#         while left <= right and list1[left] <= pivot:
#             left = left + 1
#         while left <= right and list1[right] >= pivot:
#             right = right - 1
#         if right < left:   #swap pivot with left when pivot is last and also when cond 1 fails
#             break          #now to avoid the while True loop to be infintie we have break out of the loop and swap val of pivot 
#         else:              #swap left and right when cond 2 and 3 fails
#             list1[left], list1[right] = list1[right], list1[left]
#     list1[left], list1[last] = list1[last], list1[left]   #swapping pivot with left, and coming out of the function because pivot reach the correct position now have to divide and conquer
#     return left         #here returning the pivot val

# def quicksort(list1, first, last):
#     if first < last:    #run until this cond is true, because we want it to run until and unless first == last
#         p = pivot_place(list1, first, last)
#         quicksort(list1, first, p-1)  #for left side of pivot val, it divides and sort and goes on
#         quicksort(list1, p+1, last)   #for right side of pivot val, it divides and sort and goes on

# #input
# list1 = [6,5,4,100,2,1,1,1,0]
# n = len(list1)
# quicksort(list1, 0, n -1)
# print(list1)



# # With medain as pivot and then last

# import statistics
# def pivot_place(list1, first, last):
#     low = list1[first]
#     high = list1[last]
#     mid = (first+last)//2
#     pivot_val = statistics.median([low,list1[mid],high])
#     if pivot_val == low:
#         pindex = first
#     elif pivot_val == high:
#         pindex = last
#     else:
#         pindex = mid
#     # print(pindex)
#     list1[pindex], list1[last] = list1[last], list1[pindex]

#     pivot = list1[last]
#     left = first
#     right = last - 1
#     while True:    #if cond 2 and 3 fails we will swap val of left and right and check or start once again where it was on, so this loop is for that purpose
#         while left <= right and list1[left] <= pivot:
#             left = left + 1
#         while left <= right and list1[right] >= pivot:
#             right = right - 1
#         if right < left:   #swap pivot with left when pivot is last and also when cond 1 fails
#             break          #now to avoid the while True loop to be infintie we have break out of the loop and swap val of pivot 
#         else:              #swap left and right when cond 2 and 3 fails
#             list1[left], list1[right] = list1[right], list1[left]
#     list1[left], list1[last] = list1[last], list1[left]   #swapping pivot with left, and coming out of the function because pivot reach the correct position now have to divide and conquer
#     return left         #here returning the pivot val

# def quicksort(list1, first, last):
#     if first < last:    #run until this cond is true, because we want it to run until and unless first == last
#         p = pivot_place(list1, first, last)
#         quicksort(list1, first, p-1)  #for left side of pivot val, it divides and sort and goes on
#         quicksort(list1, p+1, last)   #for right side of pivot val, it divides and sort and goes on

# #input
# list1 = [600,5,4,100,2,1,1,1,0]
# n = len(list1)
# quicksort(list1, 0, n -1)
# print(list1)


# Q: Palindromic prime number

# # for prime number

# num = 1
# if num > 1: 
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else: 
#         print(num, "is a prime number")

# # for palindrome number

# numb = 222122
# reversed_numb = int(str(numb)[::-1])
# # print(reversed_numb)
# if numb == reversed_numb:
#     print(f"The number {numb} is palindromic")
# else:
#     print(f"The number {numb} is not a palindromic number")

# # combine

# lower_limit = int(input("enter the first number: "))
# upper_limit = int(input("enter the second number: "))

# for num in range (lower_limit, upper_limit+1):
#     reversed_numb = int(str(num)[::-1])
#     if num == reversed_numb:
#     # print(f"The number {num} is palindromic")
#         if num > 1: 
#             for i in range(2, num):
#                 if num % i == 0:
#                     # print(num, "is palindrome but not a prime number")
#                     break
#             else: 
#                 print(num)
#                 # print(num, "is palindromic prime number")
#     # else:
#     #     if num > 1: 
#     #         for i in range(2, num):
#     #             if num % i == 0:
#     #                 print(num, "is neither palindrome nor a prime number")
#     #                 break
#     #         else: 
#     #             print(num, "is not a palindrome but a prime number")
#     #         # print(f"The number {num} is not a palindromic number")

# # Q: Count no of vowels in a sentence

# sen = 'HEllooo0'
# a = sen.lower()
# b = ["a", "e", "i", "o", "u"]
# d = []
# count = 0
# for i in a:
#     # print(i)
#     # for j in b:
#     #     print(i, j)
#     #     if i == j:
#     #         count += 1
#     #         d.append(i)
#     #         break
#     if i in b:
#         count +=1
#         d.append(i)
# print(f"There are {count} vowels in a sentence count which are {d}")


# Q: for printing indexes of duplicate val in a list

# list1 = [1,2,3,2,4,4,2]
# result = []
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] == list1[j]:
#             if i not in result:
#                 result.append(i)
#             if j not in result:
#                 result.append(j)

# print(*result)  #*remove bracket and print sep val 

# # using list comprenhension method

# list2 = [i for i in range(len(list1)) if list1[i]== 0]
# print(*list2)


# # Q: BinarySearch

# def BinarySearch (list1, key):
#     low = 0
#     high = len(list1)-1
#     Found = False
#     result = []
#     while low <= high and not Found:
#         mid = (low + high) // 2
#         # print(mid)
#         if key == list1[mid]:
#             Found = True
#             result.append(mid)
#         elif key > list1[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#     if Found == True:
#         print("key found at", *result )
#     else:
#         print("key not found")

# list1 = [23, 0, 1, 4, 3, 7, 3]
# list1.sort()
# print(list1)
# BinarySearch(list1, 3)


# # Q: Anagram program

# a = input("Enter 1st word you need to know is Anagram or not: ")
# b = input("Enter 2nd word you need to know is Anagram or not: ")
# # using sorting function

# sorted_a, sorted_b = sorted(a), sorted(b)

# if len(a) == len(b):
#     if sorted_a == sorted_b:
#         print("The given words are Anagram")
#     else:
#         print("The words are not Anagram")
# else:
#     print("Both strings are not even same in length how they can be Anagram?")

# # using sorting 
# c, d = list(a), list(b)
# print(c,d)

# for i in range(len(c)):
#     m_index = i
#     for j in range(i+1, len(c)):
#         if c[j] < c[m_index]:
#             m_index = j
#     c[i], c[m_index] = c[m_index], c[i]

# print(c)   

# for i in range(len(d)):
#     m_index = i
#     for j in range(i+1, len(d)):
#         if d[j] < d[m_index]:
#             m_index = j
#     d[i], d[m_index] = d[m_index], d[i]

# print(d)   

# if c == d:
#     print("it's Anagram")


# Q: Co-prime number program

# n1 = int(input("Enter the 1st number for GCD: "))
# n2 = int(input("Enter the 1st number for GCD: "))


# a = []
# b = []
# c = []

# for no1 in range(1,n1+1):
#     if n1%no1 == 0:
#         a.append(no1)
# for no2 in range(1,n2+1):
#     if n2%no2 == 0:
#         b.append(no2)

# for val in a:
#     if val in b:
#         c.append(val)
        
# print(c)
# if len(c) > 1:
#     print("These are not a Co-prime numbers")
# elif len(c) <= 0:
#     print("Please try again and provide numbers greater than zero")
# else:
#     print("These are the Co-prime numbers")

# Q: using in built library

# import math

# a = math.gcd(22,23)

# if a > 1:
#     print("Numbers are not Co-prime as the GCD is", a)
# else:
#     print("Numbers are Co-Prime, the GCD is", a)


# Co prime number for a given number

# def impute_gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         # print(b)
#         return impute_gcd(b, a%b)
    
    
# c = impute_gcd(12,5)
# # print(c)

# but this way we won't have divisors of any number

# so for divisors

# a = 12
# for i in range(1, a+1):
#     gcd = 1
#     for j in range(1, i+1):
#         if i % j == 0 and a % j == 0:
#             gcd = j
#     if gcd == 1:
#         print(i)
                 
# num1 = int(input("Enter number: "))
# lower_limit = int(input("lower limit: "))
# upper_limit = int(input("upper limit: "))

# for i in range(lower_limit,upper_limit):
#     if math.gcd(num1, i) == 1:
#         print(i)


# Q: find the maximum value in the nested list?

# list2 = []
# def list_max(list1):
#     for i in list1:
#         if type(i) == list:
#             list_max(i)
#         else:
#             list2.append(i)
#     return max(list2), min(list2)

# list1 = [1,2,[[23,43]],23]
# c = list_max(list1)
# print(c)

#1
#2 5 
#3 6 8
#4 7 9 10

# n = int(input("Enter no of rows: "))

# for row in range(n):
#     val = row +1 #0+1
#     dec = n - 1  #4-1=3
#     for col in range(row+1):
#         print(val, end=" ")
#         val = val + dec  #0+3=3
#         dec = dec - 1    #3-1 =2
#     print()

# Q: printing in reversed pattern staring from highest val and ending with 1.

# def num(n1):
#     if n1 == 1:
#         return 1
#     else:
#         return n1 + num(n1-1)
    
# a = num(n)   #for getting the first digit
# for row in range(n):  #no of rows
#     val = a - row    #
#     dec = n - 1
#     for col in range(row+1):  #no of columns
#         print(format(val, '<3'), end=" ")  
#         val = val - dec
#         dec = dec - 1
#     print()

# Q: guess the output

# for i in sorted([10,20,30,2,0,1,90,1], reverse = True):
#     print(i)

# for i in sorted([10,20,30,2,0,1,90,1])[::-1]:
#     print(i)

# for i in [10,2,3,0,90].sort():
#     print(i)


# Q: leap year?

# year = int(input("Enter year number you want to know is a leap year or not: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year, "Leap year")
# else:
#     print(year, "Not a leap year")
# Print()

# For Date to check id it's Palindrome or not

# date = input("Enter the date in DD/MM/YYYY format: ")
# given_date = date.replace("/", "")
# reverse_date = given_date [::-1]
# if given_date == reverse_date:
#     print(date, "is Palindrome")
# else:
#     print(date, "is not Palindrome")



# Q: Armstrong number

# n = int(input("Enter Number you need to know is Armstrong or not: "))

# # store the digit val with it's cube
# store = 0 
# # store the orginal n
# orginal = n
# # for number of digits
# dig = len(str(n))

# for i in range(dig):
#     # print(n)
#     a = n % 10  #153%10 = 3, 15%10 = 5, 1%10 = 1
#     store = store + (a**dig)
#     # print(store)
#     b = n // 10  #153//10 = 15, 15 // 10 = 1, 1 // 10 = 0
#     n = b        #15, 1

# if orginal == store:
#     print(orginal, "is an Armstrong number")
# else:
#     print(orginal, "not an Armstrong number")

    
    

# # Q: printing star patterns

# n = int(input("Enter number of rows: "))

# for row in range(1, n+1):
#     for col in range(1, row+1):
#         print(format("*", "<1"), end = " ")
#     print()

# # 2nd pattern

# for row in range(n):
#     spc = n - 1 - row #3-1-0=2
#     str = row + 1
#     for sp in range(spc):
#         print(end = " ")
#     for st in range(str):
#         print("*", end= "")
#     print()

# # 3rd pattern reverse

# for row in range(n):
#     for col in range(n, row, -1):
#         print(format("*", "<1"), end = " ")
#     print()

# # 4th pattern reverse

# for row in range(n, 0, -1):
#     spc = n - row #3-3=0, 3-2=1, 3-1=2
#     for sp in range(spc):
#         print(end = " ")
#     for st in range(row):
#         print("*", end= "")
#     print()


# # 5th pattern program for string printing

# sta = input("Enter string: ")
# for row in range(len(sta)):
#     for col in range(row+1):
#         print(format(sta[col], "<1"), end = " ")
#     print()


# # Q: Factorial recurssion

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return  n * factorial(n-1)

# print(factorial(5))

# # using loops
# n = 5
# result = 1
# while n >= 1:
#     result = result * n
#     n = n - 1
# print(result)


#Q: Fabonacci series?
# 0, 1, 1, 2, 3, 5, 8, 13....

# a = 0
# b = 1
# a + b = 0 + 1 = 1
# a = b 1
# b = a + b 1 + 1 = 2
# a = b 2
# b = a + b 1 + 2 = 3

# num = int(input("Enter the number to where you want the series: "))

# a, b = 0, 1

# for i in range(num):
#     print(a, end = " ")
#     temp = a + b # 0 + 1 = 1, 1 + 1
#     a = b # 1
#     b = temp #1

# print()

# # Q: prime numbers

# if num >= 1:
#     for i in range(2, num):
#         if num % i == 0: #5%1=
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print("Pick no >= 1")


# Q: Interview question flames game

# name1 = input("Enter the 1st name: ").lower()
# name2 = input("Enter the 2nd name: ").lower()
# name1 = name1.replace(" ", "")
# name2 = name2.replace(" ", "")
# print(name1)
# print(name2)

# for i in name1:
#     for j in name2:
#         if i == j:
#             name1 = name1.replace(i, "",1) #m
#             name2 = name2.replace(j,"",1) #mx, m
#             break

# print(name1, name2)
# count = len(name1+name2)
# print(count)

# if count > 0:
#     a = ["Friends", "lovers", "Affecionate", "Marriage", "Enemy", "Siblings"]
#     while len(a) > 1:
#         c = count % len(a)
#         c_index = c - 1
#         if c_index >= 0:
#             left = a [:c_index]
#             right = a [c_index+1:]
#             a = right + left
#         else:
#             a = a [:c_index]
#     print("relationship is", a[0])
# else:
#     print("please try different names")

# a = ["Friends", "lovers", "Affecionate", "Marriage", "Enemy", "Siblings"]
# print(a [5:])

# #Fibonacci using recurssion

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(9))


# # Q: Addition and subtraction of matrix

# # taking inputs for rows and columns
# row = int(input("Enter no of rows: "))
# col = int(input("Enter no of cols: "))
# print()

# # taking inputs elements of 1st matrix using list comprehension method
# print("Enter the elements for Matrix 1: ")
# matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
# print()

# # taking inputs elements of 2nd matrix using list comprehension method
# print("Enter the elements for Matrix 2: ")
# matrix2 = [[int(input()) for i in range(col)] for j in range(row)]
# print()

# # for printing the matrix 1 in matrix format
# print("Matrix 1: \n")
# for i in range (row):
#     for j in range (col):
#         print(format(matrix1[i][j], "<3"), end = " ")
#     print()
# print()

# # for printing the matrix 2 in matrix format
# print("Matrix 2: \n")
# for i in range (row):
#     for j in range (col):
#         print(format(matrix2[i][j], "<3"), end = " ")
#     print()
# print()

# # for storing the addition
# result_A = [[0 for i in range(col)] for j in range(row)]

# # doing addtion
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         result_A [i][j] = matrix1 [i][j] + matrix2 [i][j]

# # now for printing the result in matrix format
# print("Result: \n")
# for i in range(row):
#     for j in range(col):
#         print(format(result_A [i][j], "<3"), end = " ")
#     print()


# # for storing the subtraction
# result_S = [[0 for i in range(col)] for j in range(row)]

# # doing subtraction
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         result_S [i][j] = matrix1 [i][j] - matrix2 [i][j]

# # now for printing the result in matrix format
# print("Result: \n")
# for i in range(row):
#     for j in range(col):
#         print(format(result_S [i][j], "<3"), end = " ")
#     print()
        


# matrix multiplication practice
# Q: Program for Matrix Multiplication

## key rules in mind: 
## Possible (no of cols in Matrix 1 == no of rows in Matrix 2  ## ex1: (3x2) == (2x4), ex2: (2x3) == (3x5))
## Not Possible (no of cols in Matrix 1 != no of rows in Matrix 2 ## ex1: (4x3) != (4x4), ex2: (1x2) != (3x2))

## For result format: no of rows in M1 and no of cols in M2 

## Points to keep in mind 
## multiplication possible : (pxn) == (nxq) 
## For result format : (pxq)


# taking inputs for rows and columns
p = int(input("Enter no of rows in Matrix 1: "))
q = int(input("Enter no of cols in Matrix 2: "))
n = int(input("Enter no of cols in Matrix 1 / no of row in Matrix 2: "))
print()

# taking inputs elements of 1st matrix using list comprehension method
print("Enter the elements for Matrix 1: ")
matrix1 = [[int(input()) for i in range(n)] for j in range(p)]
print()

# for printing the matrix 1 in matrix format
print("Matrix 1: \n")
for i in range (p):
    for j in range (n):
        print(format(matrix1[i][j], "<3"), end = " ")
    print()
print()


# taking inputs elements of 2nd matrix using list comprehension method
print("Enter the elements for Matrix 2: ")
matrix2 = [[int(input()) for i in range(q)] for j in range(n)]
print()

# for printing the matrix 2 in matrix format
print("Matrix 2: \n")
for i in range (n):
    for j in range (q):
        print(format(matrix2[i][j], "<3"), end = " ")
    print()
print()


# for storing the multiplication
result_m = [[0 for i in range(q)] for j in range(p)]

# doing multiplication
for i in range(p):
    for j in range(q):
        for k in range(n):
            result_m [i][j] = result_m [i][j] + matrix1 [i][k] * matrix2 [k][j]


# now for printing the result in matrix format
print("Result: \n")
for i in range(p):
    for j in range(q):
        print(format(result_m [i][j], "<3"), end = " ")
    print()
