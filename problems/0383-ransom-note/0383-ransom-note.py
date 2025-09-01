class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rans=list(ransomNote)
        mag=list(magazine)
        for n in rans:
            if n in mag: mag.remove(n)
            else: 
                return False
        return True