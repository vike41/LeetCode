class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ''
        length_1 = len(word1)
        length_2 = len(word2)
        index = 0
        while index < length_1:
            result = result + word1[index]
            result = result + word2[index]
            index = index + 1

        if length_1 < length_2:
            for x in length_1 - index:
                result = result + word1[x]
        elif length_1 > length_2:
            for x in length_1 - index:
                result = result + word2[x]
        return result


if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    solution = Solution()
    result = solution.mergeAlternately(word1, word2)
    print(result)