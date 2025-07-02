a = 10  # Naxışın başlanğıc nöqtəsidir.
for i in range(0, a):
    for j in range(a, i, -1):
        print(j, end=" ")
    print()