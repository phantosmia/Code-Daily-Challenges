def generate_largest_possible_integer(array):
    array = list(map(str, array))
    array.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(array)))

from functools import cmp_to_key

def generate_largest_possible_integer_2(array):
    array = list(map(str, array))
    
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0
    
    array.sort(key=cmp_to_key(compare))
    
    largest_num = ''.join(array)
    
    if largest_num[0] == '0':
        return '0'
    
    return largest_num

# Test case
numbers = [824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]
test_case_1 = [3, 30, 34, 5, 9]
test_case_2 = [10, 7, 76, 415]
test_case_3 = [824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]
test_case_4 = [121, 12]
test_case_5 = [9, 90, 91, 92]
test_case_6 = [3, 30, 34, 5, 9]
print(generate_largest_possible_integer(numbers))
print(generate_largest_possible_integer_2(numbers))
print(generate_largest_possible_integer(test_case_1))
print(generate_largest_possible_integer_2(test_case_1))
print(generate_largest_possible_integer(test_case_2))
print(generate_largest_possible_integer_2(test_case_2))
print(generate_largest_possible_integer(test_case_3))
print(generate_largest_possible_integer_2(test_case_3))
print(generate_largest_possible_integer(test_case_4))
print(generate_largest_possible_integer_2(test_case_4))
print(generate_largest_possible_integer(test_case_5))
print(generate_largest_possible_integer_2(test_case_5))
print(generate_largest_possible_integer(test_case_6))
print(generate_largest_possible_integer_2(test_case_6))
