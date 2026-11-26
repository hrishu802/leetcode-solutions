class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
            
        pairs = set(zip(pattern, words))
        
        return len(pairs) == len(set(pattern)) == len(set(words))
