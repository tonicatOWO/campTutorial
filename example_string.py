def string_manipulation():
    s = "Learn Competitive Programming"
    print(f"前五個字元: {s[0:5]}")  # Learn
    print(f"反轉字串: {s[::-1]}")   # gnimmargorP evititepmoC nraeL
    
    # 字串連接
    result = s + " with Python"
    print(result)

import re

def count_words(text):
    words = re.findall(r"\w+", text)
    return len(words)

text = "Learn Competitive Programming with GFG!"
print(f"字數統計: {count_words(text)}")  # 5

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
