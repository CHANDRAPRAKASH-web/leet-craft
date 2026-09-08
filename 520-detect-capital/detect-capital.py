class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        fc=True
        if ord('A')<=ord(word[0])<=ord('Z'):
            for i in range(1,len(word)):
                if ord('A')<=ord(word[i])<=ord('Z'):
                    fc=False
        else:
            fc=False
        return all(ord('A')<=ord(i)<=ord('Z') for i in word) or all(ord('a')<=ord(i)<=ord('z') for i in word) or fc
        