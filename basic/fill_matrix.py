#!/usr/bin/env python

# init: O(R * C)

def create_matrix(row_size, column_size, init): # O(r*c)
    # return [[init for col in range(column_size)] for row in range(row_size)]
    matrix = []
    for i in range(row_size):
        column = []
        for j in range(column_size):
            column.append(init)
        matrix.append(column)
    return matrix


def print_matrix(matrix):
    row_size = len(matrix)
    column_size = len(matrix[0])
    for i in range(row_size):
        print()
        for j in range(column_size):
            print(f"{matrix[i][j]}\t", end='')
    print()

def query(i, j): # O(1)
    print(f"{matrix[i][j]}\t", end='')

row_size = int(input("Get row size: "))
column_size = int(input("Get column size: "))
number = int(input("Get a number: "))
print(f"Fill matrix {row_size} x {column_size} with {number}")

matrix = create_matrix(row_size, column_size, number)
print_matrix(matrix)
query(3,4) # O(1)

