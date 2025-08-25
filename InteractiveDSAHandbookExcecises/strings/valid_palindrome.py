"""
https://leetcode.com/problems/valid-palindrome/
"""

def is_palindrome(txt):
	lower_txt = ''.join(char.lower() for char in txt if char.isalnum())
	low = 0
	high = len(lower_txt) - 1
	
	while low < high:
		if lower_txt[low] == lower_txt[high]:
			low += 1
			high -= 1
		else:
			return False
	
	return True