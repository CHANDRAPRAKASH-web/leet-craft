class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel={'a','e','i','o','u'}
        vowels=defaultdict(int)
        consonant=defaultdict(int)
        max_vowels=0
        max_consonant=0
        for i in s:
            if i in vowel:
                vowels[i]+=1
                max_vowels=max(max_vowels,vowels[i])
            else:
                consonant[i]+=1
                max_consonant=max(max_consonant,consonant[i])
        return max_vowels+max_consonant