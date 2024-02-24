def squareseq(a, b):
    start = a
    stop = b
    while start <= stop:
        yield start ** 2
        start += 1

a = int(input())
b = int(input())
square = squareseq(a,b)
for num in square:
    print(num)
