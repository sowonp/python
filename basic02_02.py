a = 5
for i in range(a):
    print('*' * (i + 1))

print()

for i in range(a):
    print(' ' * (a - (i + 1)), end = '')
    print('*' * (i + 1))

print()

for i in range(a):
    print(' ' * (a - 1 - i), end = '')
    print('*' * (2 * i + 1))