class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')
        curr_vowels=sum(1 for c in s[:k] if c in vowels)
        max_vowels=curr_vowels

        for i in range(k, len(s)):
            curr_vowels+=(s[i] in vowels)-(s[i-k] in vowels)
            max_vowels= max(max_vowels,curr_vowels)

        return max_vowels