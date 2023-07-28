""" to print first,last and central character """

# a="AmanTiwari"
#
# b=len(a)
# print(b)
# print("The first letter is",a[0])
# print("The last letter is",a[b-1])
# c=int(b/2)
# if b%2==0:
#     print("The central character is",a[c-1])
#
# else:
#     print("The central character is",a[c])

# string="AmanTiwari"
# s1=list(string)
# print(string[0],str(string[len(string)//2]),string[-1])
# print(string[-1])

""" here string to list """
# str1 = "The quick brown fox jumps over the lazy dog."
# print(str1.split(' ')) # it directly converts the string to list, here after spaces
# str1 = "The-quick-brown-fox-jumps-over-the-lazy-dog."
# a=str1.split('-')
# print(a)
""" Here, replacing of characters with new one """
# amount = "32.054,23"
# maketrans = amount.maketrans
# amount1 = amount.translate(maketrans(',.', '.,'))
# print(amount1)


# import textwrap
# string='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# a=textwrap.TextWrapper(width=3)
# b=a.wrap(text=string)
# print(b)
# for i in b:
#     print(i+",")



# n,m=map(int,input().split())
# for i in range(1,n,2):
#     print((".|."*i).center(m,"-"))
# string="WELCOME"
# print(string.center(m,"-"))
# for j in reversed(range(1,n,2)):
#     print((".|." * j).center(m, "-"))



# n=int(input("enter a number: "))
# w=len(bin(n)[2:])
# for i in range(1,n+1):
#     decimal=str(i)
#     a=list(oct(i))
#     str1=''
#     for j in a[2:]:
#         str1=str1+j
#     b=list(hex(i))
#     str2=''
#     for k in b[2:]:
#         str2=str2+k
#     c=list(bin(i))
#     str3=''
#     for m in c[2:]:
#         str3=str3+m
#     print(decimal.rjust(w),str1.rjust(w),str2.upper().rjust(w),str3.rjust(w))

# a=14
# width=len(bin(a)[:5])
# b=bin(a)
# print(b.rjust(width))
# print(b[2:])
# print(hex(a)[2:])
# print(oct(a)[2:])


#
# import string
# n=int(input("Enter a number"))
# alph=string.ascii_lowercase
# l=alph[:n]
# len=(2*n-1)+(2*n-2) #edcbabcde(2n-1) & -(2n-2)
# for i in reversed(range(1,n)):
#     p="-".join(l[i:][::-1]+l[i+1:])
#     print(p.center(len))
# for i in range(n):
#     p="-".join(l[i:][::-1]+l[i+1:])
#     print(p.center(len))



# m=int(input("enter the range number: "))
# w=len(bin(m)[:3])
# for i in range(m//2):
#     print("*".rjust(w),end=" ")
#     print("*".rjust((i*2)+1))
# print("==----------------->>>".rjust(2*m+1))
# for i in reversed(range(m//2)):
#     print("*".rjust(w),end=" ")
#     print("*".rjust((i*2)+1))

# n=int(input("Enter no. of commands:"))
# l=[]
# for i in range(n):
#     command=input(("Enter command:")).split()
#     print(command)



# """ joining characters to name """
# a="AmanTiwari"
# print("*".join(a))
""" Checking perfect square """
# import math
# x=16
# a=math.isqrt(x)
# print(a)
# if a*a == x:
#     print("Perfect square")
# else:
#     print("no")


# i=2   #Find 2nd maximum no.
# list1 = [10, 20,2, 14, 45, 45, 99,99]
# list_new=sorted(list(set(list1)), reverse=True)
# print(list_new[i-1])


# list1 = [10, 20,2, 14, 45, 45, 99,99]
# l=len(set(list1))
# list_new=sorted(list(set(list1)), reverse=True)
# print(list_new[l-(l-1)])

# x=int(input("Enter x:"))
# y=int(input("Enter y:"))
# z=int(input("Enter z:"))
# n=int(input("Enter n:"))
# print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n))

""" To find the average number of students's marks"""


# n=int(input("Enter no. of students:"))
# student_marks={}
# for i in range(n):
#     name,*line=input("Enter name and score:").split()
#     scores=list(map(float,line))
#     student_marks[name]=scores
# query_name=input("Enter name for query:")
# score_query=student_marks[query_name]
# print("Avergae marks of ",query_name,"is ",round(sum(score_query)/len(score_query),2))


# n=int(input("Enter no. of elements:"))
# t=tuple(map(int,input("Enter elements:").split()))
# print(hash(t))

# s = input("Enter String:")
# print(any(i.isalnum() for i in s))
# print(any(i.isalpha() for i in s))
# print(any(i.isdigit() for i in s))
# print(any(i.islower() for i in s))
# print(any(i.isupper() for i in s))
""" This is to dynamically add to text and dynamically print it"""
# f=input("Enter Firstname:")
# l=input("Enter Lastname:")
# m=input("Enter age")
# txt="Hello {} {} {}! You just delved into python"
# print(txt.format(f,l,m))


# string="abracadabra"
# print(string[5])
# lst=list(string)
# lst[5]="k"
# print(lst)
# new_string="".join(lst)
# print(new_string)

""" This is to add characters in between string or even list"""
# string="abracadabra"
# new_string=string[:5]+"k"+string[5:]
# print(new_string)

"""This is function for adding the letters in string"""
# def mutable_string(string,index,character):
#     new_string=string[:index]+character+string[index+1:]
#     return new_string
# x=mutable_string("abracadabra",5,"k")
# print(x)

"""This is to check a part of string is present into other string or not"""
# string="ABCDCDC"
# substring="CDC"
# count=0
# for i in range(len(string)):
#     if string[i:len(string)].startswith(substring):
#         count+=1
# print(count)
# if substring in string:
#     print("ok")
# else:
#     print("Chal")

#--14-- Welcome design
# N=int(input("Enter N:"))  #N is an odd natural number
# M=3*N
# d=".|."
# print(N//2)
# for i in range(N//2):
#     j=i*2+1
#     print((d*j).center(M,"-"))
# print("WELCOME".center(M,"-"))
# for i in reversed(range(N//2)):
#     j = i * 2 + 1
#     print((d*j).center(M,"-"))
# list=[1,2,3,4,5,6]
# # for _ in list:
# #     print(_)
# for _ in reversed(list):
#     print(_)

# import string
# n=int(input("Enter an integer"))
# alph=string.ascii_lowercase
# l=alph[:n]
# print(l)
# len=(2*n-1)+(2*n-2)         #edcbabcde(2n-1) & -(2n-2)
# for i in reversed(range(1,n)):
#     p="-".join(l[i:][::-1]+l[i+1:])
#     print(p.center(len))
# for i in range(n):
#     p="-".join(l[i:][::-1]+l[i+1:])
#     print(p.center(len))
#import string
# a="12345.0"
# print(a.zfill(10))

# txt = '1234'
# print('Original string:', txt)
# print('New string:', txt.rjust(8, '0'))


# print('Original string:', txt)
# print('New string:', txt.ljust(20, '0'))
# print(txt.zfill(30))



# txt="sjdcbsdkjvbsdAmanAA@#$%\]0763"
# list=[]
# str=''
# for i in txt:
#     if i.isnumeric():
#         list.append(i)
#         str=str+i
#
# print(list)
# print(str)



str="[@_!#$%^&*()<>?/\|}{~:]')"
string="sjdcbsdkjvbsdAmanAA@#$%\]0763"
str1=""
for i in string:
    if i in str:
        str1=str1+i

print(str1)
if len(str1)<5:
    print("Its lenght is less than 5")
else:
    print("It is more than 5")

print(len(str1))























