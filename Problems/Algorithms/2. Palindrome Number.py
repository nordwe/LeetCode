# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):
     # Convert the number to a string
        x_str = str(x)
        
        # Check if the string is equal to its reverse
        return x_str == x_str[::-1]
