# import random
# import math
# # randomlist = []
# # for i in range(0,5):
# #     n = random.randint(1,100)
# #     randomlist.append(n)
# # print(randomlist)
# #
# # def nearest_int(num):
# #     sqrt = math.isqrt(num)
# #     return sqrt
# # sqroot_with_no_decimal = [nearest_int(num) for num in randomlist]
# # print("Square root list:", sqroot_with_no_decimal)
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
def is_symmetrical(string):
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            return False
    return True

def isPalindrome(string):

    if (string == string[::-1]):
        return True
    else:
        return False

string = "madam"
if is_symmetrical(string) == True and isPalindrome(string)== True:
    print("The string is symmetrical and palindrone")

