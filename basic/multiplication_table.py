#!/usr/bin/env python

# O(n^2)

print("Multiplication table:")

for n in range(2, 10 + 1):
    print()
    for i in range(1, 10 + 1):
        print(f'{n * i}\t', end='')
print()
