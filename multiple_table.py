a = int(input())
b = int(input())
c = int(input())
d = int(input())
print()
for k in range(c, d + 1):
    print(' ',k, end=' ')
print()
for i in range(a, b + 1):
    print(i, end=' ')
    for j in range(c, d + 1):
        if i*j < 10:
            print(' ', end='')
        print(i * j, end=' ')
    print()
