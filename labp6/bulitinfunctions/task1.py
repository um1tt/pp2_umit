import math

def multiplication(numbers):
    return math.prod(numbers)

input_str = input()
numbers = list(map(int, input_str.split()))
result = multiplication(numbers)
print(result)
