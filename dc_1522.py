from collections import defaultdict


def find_substring_indices(s, words):
    if not s or not words:
        return []

    total_length = sum(len(word) for word in words)
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    
    result_indices = []
    for i in range(len(s) - total_length + 1):  # Ensures we don't go out of bounds
        seen_words = defaultdict(int)
        j = i
        while j < i + total_length:
            matched = False
            for word in words:
                word_length = len(word)
                if s[j:j + word_length] == word:
                    seen_words[word] += 1
                    if seen_words[word] > word_count[word]:
                        break
                    j += word_length
                    matched = True
                    break
            if not matched:
                break
        if seen_words == word_count:
            result_indices.append(i)
    
    return result_indices

print(find_substring_indices("dogcatcatcodecatdog", ["cat", "dog"]))  # Output: [0, 13]
print(find_substring_indices("barfoobazbitbyte", ["dog", "cat"]))      # Output: []
print(find_substring_indices("lingmindragon", ["mind", "dragon"]))  