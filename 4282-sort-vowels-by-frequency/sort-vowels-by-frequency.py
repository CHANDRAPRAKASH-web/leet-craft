class Solution:
    def sortVowels(self, s: str) -> str:
        vowel={'a','e','i','o','u'}
        a=defaultdict(int)
        for i in s:
            if i in vowel:
                a[i]+=1
        vowels=dict(sorted(a.items(),key=lambda item:item[1],reverse=True))
        res=[]
        for i in range(len(s)):
            if s[i] not in vowel:
                res.append(s[i])
            else:
                value=list(vowels)[0]
                res.append(value)
                vowels[value]-=1
                if vowels[value]==0:
                    del vowels[value]
        return "".join(res)


        