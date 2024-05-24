def find_all_occurrences(word, pattern):
    
    if not pattern or pattern == '':
        return []
    if len(pattern) > len(word):
        return []
    
    pattern_array = list(pattern)
    word_array = list(word)
    indexes = []
    current_index_pattern_array = 0
    length_pattern_array = len(pattern_array)
    index_of_first_char_occurrence = 0

    for index, char in enumerate(word_array):
        if char == pattern_array[current_index_pattern_array] and current_index_pattern_array == length_pattern_array - 1:
            indexes.append(index_of_first_char_occurrence)
            current_index_pattern_array = 0
        elif char == pattern_array[current_index_pattern_array]:
            if current_index_pattern_array == 0:
                index_of_first_char_occurrence = index
            current_index_pattern_array += 1
        else:
            current_index_pattern_array = 0
            index_of_first_char_occurrence = 0
    return indexes

test_cases = [
    ("abracadabra", "abr", [0, 7]),
    ("aaaaa", "aa", [0, 1, 2, 3]),
    ("hello world", "bye", []),
    ("pattern", "pattern", [0]),
    ("text", "", []),
    ("", "pattern", []),
    ("", "", []),
    ("a", "a", [0]),
    ("short", "longerpattern", []),
    ("abc$def$ghi", "$d", [3])
]

# Running test cases
for i, (word, pattern, expected) in enumerate(test_cases):
    result = find_all_occurrences(word, pattern)
    print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
    print(f"  Word: '{word}', Pattern: '{pattern}'")
    print(f"  Expected: {expected}, Got: {result}\n")

#CHATGPT solution:

def find_all_occurences(word, pattern):
    if not pattern:
        return []
    indexes = []
    index = word.find(pattern)
    while index != -1:
        indexes.append(index)
        index = word.find(pattern, index + 1)
    return indexes

word = "abracadabra"
pattern = "abr"
print(find_all_occurrences(word, pattern))  # Output: [0, 7]

def kmp_search(word, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    lps = compute_lps(pattern)
    result = []
    i = 0
    j = 0
    while i < len(word):
        if pattern[j] == word[i]:
            i += 1
            j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(word) and pattern[j] != word[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

word = "abracadabra"
pattern = "abr"
print(kmp_search(word, pattern))  # Output: [0, 7]


