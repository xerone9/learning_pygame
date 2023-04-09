A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
B = [1, 4, 2, 7, 8, 9]

for sublist in A:
    if set(sublist).issubset(set(B)):
        print(True)
        break
else:
    print(False)