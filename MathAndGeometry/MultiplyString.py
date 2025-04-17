"""
You are given two strings num1 and num2 that represent non-negative integers.

Return the product of num1 and num2 in the form of a string.

Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.

Note: You can not use any built-in library to convert the inputs directly into integers.

Example 1:

Input: num1 = "3", num2 = "4"

Output: "12"
Example 2:

Input: num1 = "111", num2 = "222"

Output: "24642"
Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.

"""


def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == '0':
        return "0"

    num1 = num1[::-1]
    num2 = num2[::-1]

    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1)):
        for j in range(len(num2)):
            pos = i + j

            mul = int(num1[i]) * int(num2[j])

            result[pos] += mul
            if result[pos] >= 10:
                result[pos + 1] += result[pos] // 10
                result[pos] = result[pos] % 10
            
        
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return "".join(map(str, result[::-1]))


