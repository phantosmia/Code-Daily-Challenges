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
