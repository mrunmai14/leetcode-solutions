class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and convert to lowercase
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        # Check palindrome by comparing string with its reverse
        return cleaned == cleaned[::-1]