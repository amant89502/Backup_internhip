# def lonelyinteger(a):
#     a = sorted(a)
#     if len(a) < 3:
#         return a[0]
#     elif a[0] != a[1]:
#         return a[0]
#     else:
#         return lonelyinteger(a[2:])
#
# if __name__ == '__main__':
#     a = int(input())
#     b = map(int, input().strip().split(" "))
#     print(lonelyinteger(b))

def mul(i):
    return i*i
# Using the map function
x = map(mul, (3, 5, 7, 11, 13))
print (type(x))
print(list(x))
mul(5)