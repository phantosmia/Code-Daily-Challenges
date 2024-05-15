'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Implement an efficient string matching algorithm.

That is, given a string of length N and a pattern of length k, write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.

If the pattern is found, return the start index of its location. If not, return False.

'''

def KMP_search(text, pattern):
    lsp = [0] * len(pattern)
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lsp[i] = j
            i += 1
        else:
            if j != 0:
                j = lsp[j-1]
            else:
                lsp[i] = 0
                i += 1
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lsp[j-1]
            else:
                i += 1
    return False

text = "abcxabcdabcdabcy"
pattern = 'abcdabcy'
print(KMP_search(text, pattern))