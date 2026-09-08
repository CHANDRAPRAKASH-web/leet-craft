class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper=0
        for i in word:
            if ord('A')<=ord(i)<=ord('Z'):
                upper+=1
        return upper==0 or upper==len(word) or (upper==1 and ord('A')<=ord(word[0])<=ord('Z'))
        