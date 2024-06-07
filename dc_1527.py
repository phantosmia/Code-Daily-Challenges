def count_how_many_times_number_appears_in_2D_multiplication_table(n, m):
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            if (i + 1) * (j + 1) == m:
                count += 1
    return count

print(count_how_many_times_number_appears_in_2D_multiplication_table(6, 6))  # Output: 4
print(count_how_many_times_number_appears_in_2D_multiplication_table(6, 9))  # Output: 1
print(count_how_many_times_number_appears_in_2D_multiplication_table(6, 12))  # Output: 4