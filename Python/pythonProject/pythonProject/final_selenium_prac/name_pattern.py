result_str=""
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)


str=""
for Row in range(0,7):
    for Col in range(0,7):
        if (Col == 1 or Col == 5 or (Row == Col and Col != 0 and Col != 6)):
            str=str+"*"
        else:
            str=str+" "
    str=str+"\n"
print(str)