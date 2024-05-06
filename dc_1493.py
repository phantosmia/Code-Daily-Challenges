def has_pythagorean_triplet(arr):
    n = len(arr)
    if n < 3:
        return False
    arr.sort()
    for i in range(2, n):
        c = arr[i]
        a, b = 0, i - 1
        while a < b:
            sum_of_squares = arr[a] ** 2 + arr[b] ** 2
            if sum_of_squares == c ** 2:
                return True
            elif sum_of_squares < c ** 2:
                a += 1
            else:
                b -= 1
    return False

test_array = [3, 1, 4, 6, 5]
print(has_pythagorean_triplet(test_array)) # True