A = [1, 2, 3, 4, 6, 7, 8, 9]
B = [1, 2, 3, 9]

result = min([elem for elem in B if elem not in A])

print(result)