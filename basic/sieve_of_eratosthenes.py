#!/usr/bin/env python

# init: O(N log log N)
# query: O(1)

import math  # sqrt

print("Sieve of Eratosthenes")

array_size = int(input("Get list number: ")) + 1

# array =[True for col in range(array_size + 1)]
array = []
for n in range(1, array_size + 1):
    array.append(True)
i = 2
for n in range(2, int(math.sqrt(array_size))):
    if array[n] == True:
        while i * n < array_size:
            array[i * n] = False
            i = i + 1

print(f"First {array_size - 1} prime numbers : ", end='')
for i in range(2, array_size):
    if array[i] == True:
        print(f"{i}, ", end='')

while True:
    print()
    i = int(input("Query number: "))
    if array[i] == True:
        print(f"{i} is a prime number.")
    else:
        print(f"{i} is not a prime number.")
