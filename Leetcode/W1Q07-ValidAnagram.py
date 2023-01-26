class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
        # onther solution which took high time
        # for i in s:
        #     if i in t:
        #         t = t.replace(i, "", 1)
        #         continue
        #     return False
        # return False if len(t)>0 else True



"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

"""