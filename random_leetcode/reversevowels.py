"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Example 2:
Constraints:

Example 1
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A'] . On reversing the vowels, s becomes "AceCreIm" .

Example 2
Input: s = "leetcode"
Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        sl = list(s)
        i = 0
        j = len(s)-1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U'}
        while i < j:
            if sl[i] not in vowels:
                i += 1
            else:
                while j > i:
                    if sl[j] not in vowels:
                        j -=1
                    else:
                        break
                sl[i], sl[j] = sl[j], sl[i]
                i +=1
                j -=1

        return "".join(sl)


                

            
            

s = Solution()
print(s.reverseVowels("IceCreAm"))



        




            
