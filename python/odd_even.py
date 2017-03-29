input = [1, 2, 5, 6, 34, 665, 234, 56, 35, 57, 2]
even, odd = [], []

for num in input:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print (even + odd)
