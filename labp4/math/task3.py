import math
n = int(input())
a = int(input())
area = (n * pow(a, 2))/(4 * math.tan(math.pi/n))
print(round(area))
