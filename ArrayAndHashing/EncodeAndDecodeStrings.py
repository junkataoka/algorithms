
"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

def encode(strs):
    return ''.join([str(len(word)) + ':' + word for word in strs])

def decode(s):
    res = []
    i = 0
    while i < len(s):
        # split by :
        j = s.find(':', i)
        length = int(s[i:j])
        res.append(s[j + 1: j + 1 + length])
        i = j + 1 + length

# time complexity: O(n), where n is the total length of the strings in the list


