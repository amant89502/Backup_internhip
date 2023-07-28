# import random
# import math
# test_list = [9,64,729,16,81]
# print("Original list is : " + str(test_list))
# for i in range (1,5):
#     list_new = []
#     random_num = random.choice(test_list)


# random_num = random.choice(test_list)
# a = math.isqrt(random_num)
# list_new = []
# if random_num not in list_new:
#     list_new.append(a)
# print(list_new)


#print("Random selected number is : " + str(random_num))
#print(math.isqrt(random_num))
import random

# Step 1: Create the list of 5 numbers
original_list = [random.randint(1, 100) for _ in range(5)]
print("Original list:", original_list)
import math
def nearest_integer_square_root(num):
    sqrt = math.sqrt(num)
    rounded_sqrt = round(sqrt)
    return rounded_sqrt

# Step 2, 3, 4, and 5: Calculate square roots and append to a new list
square_root_list = [nearest_integer_square_root(num) for num in original_list]
print("Square root list:", square_root_list)


