# list1=[]
# for i in range(1,6):
#     list1.append(random.randint(20,70))
# print("random numbers input list: ",list1)
# list2=[]
# for j in list1:
#     list2.append(math.sqrt(j))
# print("square roots :",list2)
# list3=[]
# for k in list2:
#     list3.append(round(k))
# print("rounded square roots",list3)
# for i in range (0,5):
#     print(i)

def isPalindrome(string):

    if (string == string[::-1]):
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."
string=input("Enterstring:")

print(isPalindrome(string))


def symmetry(a):
    n = len(a)
    flag = 0

    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2

    start1 = 0
    start2 = mid

    while (start1 < mid and start2 < n):

        if (a[start1] == a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break