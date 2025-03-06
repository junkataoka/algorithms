"""
Letter Combinations of a Phone Number
Solved 
You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may return the answer in any order.



Example 1:

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
Example 2:

Input: digits = ""

Output: []
Constraints:

0 <= digits.length <= 4
2 <= digits[i] <= 9

"""

def letterCombinations(digits):
    if not digits:
        return []

    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    res = []
    def backtrack(idx, path):
        if idx == len(digits):
            res.append(path)
            return

        for letter in phone[digits[idx]]:
            backtrack(idx + 1, path + letter)

    backtrack(0, '')
