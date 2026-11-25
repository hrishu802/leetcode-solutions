class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.strip()
        s = (s.split())
        
        i = 0 
        j = len(s) -1  

        while i < j :
            s[i] , s[j] = s[j], s[i]
            j -=1 
            i +=1 
        return " ".join(s)
