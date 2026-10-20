class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag_counts = Counter(magazine)
        note_counts = Counter(ransomNote)
        
        for char, count in note_counts.items():
            if count > mag_counts[char]:
                return False
                
        return True