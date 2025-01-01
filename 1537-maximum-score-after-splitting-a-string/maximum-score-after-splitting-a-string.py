class Solution:
    def maxScore(self, s: str) -> int:
        one=0
        zero=0
        sums=0
        for n in s:
            if n=='1':
                one+=1
        for i in range(len(s)-1):
            if s[i]=='0':
                zero+=1
            else:
                one-=1
            sums=max(sums,one+zero)
        return sums