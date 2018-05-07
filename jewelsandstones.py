
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
