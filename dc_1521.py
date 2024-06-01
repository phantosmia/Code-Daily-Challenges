from collections import Counter

def find_anagrams(word, string):

    len_word = len(word)
    len_string = len(string)
    result = []

    if len_word > len_string:
        return result
    
    word_counter = Counter(word)

    window_counter = Counter(string[:len_word])

    if word_counter == window_counter:
        result.append(0)
    
    for i in range(1, len_string - len_word + 1):
        start_char = string[i - 1]
        end_char = string[i + len_word - 1]

        window_counter[start_char] -= 1
        if window_counter[start_char] == 0:
            del window_counter[start_char]
        
        window_counter[end_char] += 1

        if word_counter == window_counter:
            result.append(i)
    return result

W = "ab"
S = "abxaba"
print(find_anagrams(W, S)) 