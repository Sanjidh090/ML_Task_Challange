#one liner solution
# print([i**2 for i in range(1, 11) if i %2 == 0])
 #cleaner solution
num = [i for i in range(1, 11)]
print([i**2 for i in num if i % 2 == 0])