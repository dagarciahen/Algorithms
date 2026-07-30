"""
Given two strings, s and t , both consisting of lowercase English letters, return the number of substrings in s that are anagrams of t.

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
"""

s = 'caabab'
t = 'aba'
#output should be 2 
def substring_anagram(s: str, t: str) -> int:
    len_s = len(s)
    len_t = len(t)

    if len_s < len_t:
        return 0

    expected_freq = [0]*26
    window = [0]*26

    for c in t:
        expected_freq[ord(c)-ord('a')] += 1
    l = r = 0
    count = 0

    while r < len_s:
        window[ord(s[r])-ord('a')] +=1
        if r - l +1 == len_t:
            if window == expected_freq:
                count += 1

            window[ord(s[l])-ord('a')] -= 1
            l += 1
        r += 1
    return count

def substring_anagram2(s: str, t:str) -> int:
    len_s = len(s)
    len_t = len(t)

    if len_s < len_t:
        return 0
    c = 0
    r = l = 0
    substring = ""
    while r < len_s:
        substring += s[r]
        if r - l +1 == len_t:
            if ''.join(sorted(substring)) == ''.join(sorted(t)):
                c += 1
            substring = substring[1:]
            l += 1
        r +=1
    return c




    
print(substring_anagram(s,t))
print(substring_anagram2(s,t))









