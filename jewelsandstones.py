class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        jewel = list(J)
        stone = list(S)
        for s in range(len(stone)):
            for j in range(len(jewel)):
                if stone[s] == jewel[j]:
                    count +=1
        return count

J = "aA"
S = "aAAbbbb"
ans = Solution()
ans.numJewelsInStones(J,S)
'''
另一個我很喜歡的答案
def jewels(S, J):
    jewels = {x: 0 for x in J}
    for char in S:
        if char in jewels.keys():
            jewels[char] += 1

    return sum(jewels.values())

J = "aZAb"
S = "aAAizbbbbc"
jewels(S,J)
'''
