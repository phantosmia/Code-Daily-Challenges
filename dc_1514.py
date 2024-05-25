
def chatgpt_longest_distinct_subarray(array):

    if not array:
        return 0

    last_occurrence = {}
    start = 0
    max_length = 0

    for end in range(len(array)):
        if array[end] in last_occurrence and last_occurrence[array[end]] >= start:
            start = last_occurrence[array[end]] + 1
        last_occurrence[array[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

def geeks_for_geeks_solution(a, n):
    from collections import defaultdict

    index = defaultdict(lambda: 0)

    ans = 0
    j = 0

    for i in range(n):
        j = max(index[a[i]], j)
        ans = max(ans, i - j + 1)
        index[a[i]] = i + 1
        i += 1
    return ans

test_cases = [
    ([1, 2, 3, 4, 5], 5),  # Test case 1
    ([1, 2, 2, 3, 4, 5], 4),  # Test case 2
    ([1, 2, 3, 1, 2, 3, 4, 5], 5),  # Test case 3
    ([1, 1, 1, 1, 1], 1),  # Test case 4
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),  # Test case 5
    ([5, 5, 5, 5, 5, 5], 1),  # Test case 6
    ([1, 2, 3, 2, 2, 2, 4, 5], 3),  # Test case 7
    ([1, 2, 3, 4, 5, 2, 1, 6, 7, 8], 8),  # Test case 8
    ([], 0),  # Test case 9
    ([2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9], 2),  # Test case 10
    ([1, 4, 3, 2, 4, 2, 8, 1, 9], 5)  # Test case 11
]

for i, (array, expected) in enumerate(test_cases):
    result = longest_distinct_subarray(array)
    print(f"Test Case {i + 1}: {'Passed' if result == expected else 'Failed'} - Expected {expected}, Got {result}")

print("\nChatGPT Solution\n")

for i, (array, expected) in enumerate(test_cases):
    result = chatgpt_longest_distinct_subarray(array)
    print(f"Test Case {i + 1}: {'Passed' if result == expected else 'Failed'} - Expected {expected}, Got {result}")

print("\nGeeksForGeeks Solution\n")

for i, (array, expected) in enumerate(test_cases):
    result = geeks_for_geeks_solution(array, len(array))
    print(f"Test Case {i + 1}: {'Passed' if result == expected else 'Failed'} - Expected {expected}, Got {result}")