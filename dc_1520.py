def find_unique_number(array):
    array.sort()
    for i in range(0, len(array)):
        if i == 0:
            if array[i] != array[i + 1]:
                return array[i]
        if i == len(array) - 1:
            if array[i] != array[i - 1]:
                return array[i]
        elif array[i] != array[i - 1] and array[i] != array[i + 1]:
            return array[i]

    return None

print(find_unique_number([6, 1, 3, 3, 3, 6, 6]))
print(find_unique_number([13, 19, 13, 13]))

def find_unique_number(array):
    # Initialize variables to hold the sum of bits
    ones = 0
    twos = 0
    
    for number in array:
        # `twos` holds the bits which appear twice
        twos |= ones & number
        
        # `ones` holds the bits which appear once
        ones ^= number
        
        # `common_bit_mask` contains all the bits that appeared three times
        common_bit_mask = ~(ones & twos)
        
        # Remove the common bits (those appearing three times) from `ones` and `twos`
        ones &= common_bit_mask
        twos &= common_bit_mask
        
    return ones

print(find_unique_number([6, 1, 3, 3, 3, 6, 6]))  # Output: 1
print(find_unique_number([13, 19, 13, 13]))  # Output: 19
