from random import randint

numbers1 = [randint(0,9999) for i in range(randint(50, 101))]
numbers2 = [randint(0,9999) for i in range(randint(50, 101))]
final = []
for i in numbers1:
    for j in numbers2:
        if i == j:
            final.append(i)

print(final)