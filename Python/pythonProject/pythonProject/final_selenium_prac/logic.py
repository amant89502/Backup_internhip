
result_str=""
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)

for row in range(6):
        for column in range(6):
            # first column
            if ((column == 0 or
                    # last column
                    column == 6-1) or

                    # right slanting line
                    row + column == (6 - 1) and row < 6/2 or

                    # left slanting line
                    row == column and row < 6/2
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


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



