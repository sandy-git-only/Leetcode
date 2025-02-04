class Solution(object):
    def insert_1(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i_s, i_e = 0, 1
        n_s, n_e = newInterval[0], newInterval[1]
        left = []
        right = []
        for interval in intervals:

            # 目前的區間結束值 比 新的區間開始值 小   
            if interval[i_e] < n_s:
                left.append(interval)
            # 目前的區間開始值 比 新的區間結束值 大
            elif interval[i_s] > n_e:
                right.append(interval)
            else:
                n_s = min(n_s, interval[i_s])
                n_e = max(n_e, interval[i_e])
        return left + [[n_s, n_e]] + right
    
    def insert_2(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        result = []
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        result.append([newInterval[0], newInterval[1]])

        while i < n:
            result.append(intervals[i])
            i += 1

        return result

solution = Solution()
print(solution.insert_1([[1,3],[6,9]], [2,5]))
print(solution.insert_1([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(solution.insert_2([[1,3],[6,9]], [2,5]))
print(solution.insert_2([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))