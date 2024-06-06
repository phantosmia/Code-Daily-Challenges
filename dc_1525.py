def valid_utf8(data):
    n = len(data)
    i = 0

    while i < n:
        byte1 = data[i]

        if byte1 >> 7 == 0:
            num_bytes = 1
        
        elif byte1 >> 5 == 0b110:
            num_bytes = 2
        
        elif byte1 >> 4 == 0b1110:
            num_bytes = 3
        
        elif byte1 >> 3 == 0b11110:
            num_bytes = 4

        else:
            return False
        
        for j in range(1, num_bytes):
            if i + j >= n:
                return False
            if data[i + j] >> 6 != 0b10:
                return False
        i += num_bytes

    return True

data = [0b11100010, 0b10000010, 0b10101100]  # Example for the Euro sign €
print(valid_utf8(data))