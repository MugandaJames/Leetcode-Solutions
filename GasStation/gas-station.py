class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # Impossible overall
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0

        for i in range(len(gas)):

            tank += gas[i] - cost[i]

            # Can't reach next station
            if tank < 0:
                start = i + 1
                tank = 0

        return start
