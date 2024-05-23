def first_recurring_character(word):
    seen = set()
    for char in word:
        if char in seen:
            return char
        seen.add(char)
    return None

print(first_recurring_character("interviewquery"))  # Output: i
print(first_recurring_character("interv"))  # Output: None
print(first_recurring_character("acbbac"))  # Output: i

