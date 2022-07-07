matrix = ((1, -2, 5, 20), (0, 2, 3, 400), (100, 2, 3, 4))

numbers_max = 0
numbers_sum = 0

for index, row in enumerate(matrix):
    print(index, row) 
    if numbers_max < max(row):
        numbers_max = max(row)
    numbers_sum += sum(row)

print(f"maximal={numbers_max}, summation={numbers_sum}")
