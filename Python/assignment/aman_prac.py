# print("Hello\"Hello there\" aman")


# program to print the numbers that are divisible by 15 in a particular range.
# count = 0
# for i in range(2000,3000):
#     if i%3==0 and i%5==0:
#         count=count+1
# print(count)


# to find the prime numbers in particular range
# for val in range(1, 1000):
#   if val > 1:
#     for i in range(2, val):
#       if (val % i) == 0:
#         break
#     else:
#       print(val)

#A canteen requires 28 dozen bananas for a week. How many bananas will it require for 47 days?

#print  numbers of even numbers by user input
# a = int(input("Enter a number of even numbers upto where you want to print"))
# for i in range (a*2):
#   if i%2==0:
#     print(i)

#sort the dictionary by keys and print whole sorted dictionary

# dict={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# key = list(dict.keys())
# key.sort()
# dict_sorted = {i: dict[i] for i in key}
#
# print(dict_sorted)
# num_list = input("Enter a series of numbers, separated by spaces: ").split()
# program to find the recursive letters in a string nd store it in a list

# str="geeksforgeeks"
# list=[]
# list2=[]
# for i in str:
#     if i not in list:
#         list.append(i)
#     else:
#         if i not in list2:
#             list2.append(i)
# print(list2)
# print(list)
# def reversed_string(text):
#   result = ""
#   for char in text:
#     result = char + result
#     #result = result + char
#
#   print(result)
# a=input("Enter number or word:-")
# reversed_string(a)

#A canteen requires 28 dozen bananas for a week. How many bananas will it require for 47 days?
# a = int(input("Enter how many dozen bananas are required for a week..:"))
# b = int(input("Enter for how many days you need to find the number of bananas..:"))
# c = (a/7)*12
# print("Number of bananas for", b, " days are", c*47)


#Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# a=int(input("Enter an integer to find the sqrt"))
# b=sqrt(a)
# print(b)

def sqrt(x):
  if x == 0:
    return 0

  left, right = 1, x
  while left <= right:
    mid = (left + right) // 2
    if mid * mid == x:
      print(mid)
    elif mid * mid < x:
      left = mid + 1
    else:
      right = mid - 1

  print(right)

  sqrt(144)



