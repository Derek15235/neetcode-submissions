class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexStack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if (len(indexStack)) == 0:
                indexStack.append(i)
                continue

            while indexStack and temperatures[i] > temperatures[indexStack[-1]]:
                res[indexStack[-1]] = i - indexStack[-1]
                indexStack.pop()

            indexStack.append(i)
        return res
            