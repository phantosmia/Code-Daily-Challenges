def product_off_all_elements_except_self(array):

    n = len(array)

    if n == 0:
        return []
    
    left_product = [1] * n
    right_product = [1] * n

    result = [1] * n

    for i in range(1, n):
        left_product[i] = left_product[i - 1] * array[i - 1]

    for i in range(n - 2, -1, -1):
        right_product[i] = right_product[i + 1] * array[i + 1]
    
    for i in range(n):
        result[i] = left_product[i] * right_product[i]

    return result

input_array = [1, 2, 3, 4, 5]
print(product_off_all_elements_except_self(input_array))
input_array = [3, 2, 1]
print(product_off_all_elements_except_self(input_array))
input_array = [1, 2, 3, 0, 5]
print(product_off_all_elements_except_self(input_array))

def product_except_self_division(array):
    total_product = 1
    for num in array:
        total_product *= num
    result = []
    for num in array:
        result.append(total_product // num)
    return result

input_array = [1, 2, 3, 4, 5]
print(product_except_self_division(input_array))
input_array = [3, 2, 1]
print(product_except_self_division(input_array))
# input_array = [1, 2, 3, 0, 5]
# print(product_except_self_division(input_array)) division method will not work for this case

## most optimized way

def product_except_self(nums):
    n = len(nums)
    if n == 0:
        return []

    # Initialize the result array with 1s
    result = [1] * n

    # First pass: calculate the left products and store in result
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Second pass: calculate the right products and multiply with the result
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Test Cases
test_cases = [
    ([4, 0, 2], [0, 8, 0]),
    ([0, 2, 0, 5], [0, 0, 0, 0]),
    ([1, 5], [5, 1]),
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([-1, 2, -3, 4], [-24, 12, -8, 6])
]

# Running the tests
for input_array, expected_output in test_cases:
    result = product_except_self(input_array)
    assert result == expected_output, f"Test failed for input {input_array}: expected {expected_output}, got {result}"
    print(f"Test passed for input {input_array}: {result}")


