import random

# Generate a list of 5 random two-digit numbers without using '_' and random.sample
random_two_digit_list = [random.randint(10, 99) for i in range(5)]
print(random_two_digit_list)
