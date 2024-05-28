def reverse_words(s):
    words = s.split()
    return ' '.join(words[::-1])

s = "the sky is blue"
print(reverse_words(s))
s = "hello world here"
print(reverse_words(s))

def reverse_words_in_place(s):
    s.reverse()
    start = 0
    for end, char in enumerate(s):
        if char == ' ':
            s[start:end] = reversed(s[start:end])
            start = end + 1
    s[start:] = reversed(s[start:])

s = list("the sky is blue")
reverse_words_in_place(s)
print(''.join(s))