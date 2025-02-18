# https://leetcode.com/problems/roman-to-integer/description/


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for numeral in reversed(s):
            current_value = roman_values[numeral]
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value
        return total


if __name__ == '__main__':
    solution = Solution()
    string = "MCMXCIV"
    result = solution.romanToInt(string)
    print(result)
    # Input: s = "MCMXCIV"
    # Output: 1994
    # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    # Symbol       Value
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000

    #  are usually written largest to smallest from left to right.
    # However, the numeral for four is not IIII. Instead, the number four is written as IV
