#!/usr/bin/env python

# init: O(N^2) ?

print("Longest common subsequence")

def print_matrix(s1, s2, matrix):
    row_size = len(matrix)
    column_size = len(matrix[0])
    print(f"\t\t", end='')
    for i in range(len(s2) + 1):
        print(f"{i}\t", end='')
    print()

    print(f"\t\t", end='')
    k = 0
    kk = 0
    print("ε\t", end='')
    for i in range(len(s2)):
        print(f"{s2[i]}\t", end='')
    for i in range(row_size):
        print()

        for j in range(column_size):
            if i == 0 and j == 0 and k < len(s1):
                print(f"{kk}\t", end='')

            if i == 0 and j == 0:
                print("ε\t", end='')
            if i > 0 and j == 0 and k < len(s1):
                print(f"{kk}\t{s1[k]}\t", end='')
                k = k + 1

            print(f"{matrix[i][j]}\t", end='')
        kk = kk + 1
    print()


def create_matrix(row_size, column_size, init):
    # return [[init for col in range(column_size)] for row in range(row_size)]
    matrix = []
    for i in range(row_size):
        column = []
        for j in range(column_size):
            column.append(init)
        matrix.append(column)
    return matrix


def lcs(S1, S2):
    m = len(S1)
    n = len(S2)
    matrix = create_matrix(n + 1, m + 1, 0)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    print_matrix(S1, S2, matrix)
    index = matrix[m][n]

    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i - 1] == S2[j - 1]:
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("\nS1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))


S1 = "XMJYAUZ"
S2 = "MZJAWXU"
# S1 = input("Get first string: ")
# S2 = input("Get second string: ")

m = len(S1)
n = len(S2)
lcs(S1, S2)
