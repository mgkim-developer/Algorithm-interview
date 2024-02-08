class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = 0

        for i in range(len(accounts)):
            tmp = 0
            for j in range(len(accounts[i])):
                tmp = tmp + accounts[i][j]
            if tmp > result:
                result = tmp

        return result
