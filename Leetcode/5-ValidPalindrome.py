class Solution:
    def isPalindrome(self, string: str) -> bool:
        string = string.lower()
        
        for s in string:
            if not s.isalnum():
                string = string.replace(s, '')

        return string == string[::-1]

        for s in string:
            if ord(s) in range(ord('a'), ord('z')+1) or ord(s) in range(ord('0'),ord('9')+1):
                pass
            else:
                string = string.replace(s, '')

        # there is onther method

        l, r = 0, len(string)-1
        while l < r:
            if l<r and self.is_alfa_num(string[l]):
                l+=1
            if l<r and self.is_alfa_num(string[r]):
                r-=1
            
            while string[l] != string[r]:
                return False

            l, r = l+1, r-1
        return True
        
    def is_alfa_num(self, s):
        return (ord('A') <= ord(s) <= ord('Z') or 
                ord('a') <= ord(s) <= ord('z') or 
                ord('0') <= ord(s) <= ord('9'))


s = Solution()

a = s.isPalindrome('akjgbsd')
print(a)



'''

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false

Input: s = " "
Output: true

'''