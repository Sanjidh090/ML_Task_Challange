import collections
s = 'silent'
t = 'listen'
def is_anagram(s, t):
    return collections.Counter(s) == collections.Counter(t)
print(is_anagram(s, t))  # Output: True
