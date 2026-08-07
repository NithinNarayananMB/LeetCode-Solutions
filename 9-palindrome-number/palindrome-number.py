class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return  True   
        if x > 0 and x % 10 != 0:
            temp = x
            rev = 0
            while temp > 0:
                  rev = rev * 10 + (temp % 10)
                  temp //= 10
            return rev == x  
        return False        