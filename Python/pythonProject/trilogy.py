N=input("Enter the value of N: ")
T=int(input("Enter the value of T: "))
temp=[]
index1=[]
main=[]
m=(len(temp)+1)*2
# print(m)
for i in N:
    temp.append('_')
    temp.append('_')
    temp.append(i)
temp.append('_')
temp.append('_')
# print(temp)
temp1=temp.copy()
for i in range(len(temp)):
    if temp[i]=='_':
        index1.append(i)
# print(index1)
for k in range(10):
    for l in range(10):
        if l!=k:
            for o in index1:
                for n in index1:
                    str1 = ""
                    temp = temp1.copy()
                    if n!=o:
                        temp[o]=k
                        temp[n]=l
                        # print(temp)
                        temp[:] = (value for value in temp if value != '_')
                        # print(temp)
                        for p in temp:
                            str1=str1+str(p)
                        num=int(str1)
                        if num%3==0:
                            main.append(num)
                            # print(main)
# print(min(main))
if T==0:
    print(min(main))

else:
    print(max(main))