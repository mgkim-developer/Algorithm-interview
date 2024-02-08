class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = Counter(ransomNote)
        magazineDict = Counter(magazine)
        for k in ransomNoteDict:
            magazineDict[k] = magazineDict.get(k, 0) - ransomNoteDict[k]
            if magazineDict[k] < 0:
                return False
        return True


