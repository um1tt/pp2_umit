import math

def upper_lower(string):
    uppercase = sum(1 for char in string if char.isupper())
    lowercase = sum(1 for char in string if char.islower())
    return uppercase, lowercase

input_str = input()
upper_count, lower_count = upper_lower(input_str)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
