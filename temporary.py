a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

for i in a:
    print("checking")
    for j in b:
        if i == 2:
            break
    else:
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner