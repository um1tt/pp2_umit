def numto0(m):
    while m >= 0:
        yield m
        m -= 1
m = int(input())
number = numto0(m)
for num in number:
    print(num)
