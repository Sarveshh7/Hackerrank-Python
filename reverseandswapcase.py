def reverse_and_swapcase(s):
    words = s.split()             # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the list of words
    # Swap case of each word using list comprehension
    swapped_case = [word.swapcase() for word in reversed_words]
    result = ' '.join(swapped_case)  # Join the words back with spaces
    return result

s = input()
print(reverse_and_swapcase(s))
