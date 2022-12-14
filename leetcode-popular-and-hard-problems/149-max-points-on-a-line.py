"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
# solution
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n < 3:
            return n
        
        ans = 0
        for i in range(n):
            dic = {'inf':0}
            samePointsNum = 0
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    samePointsNum += 1
                    continue
                if x1 == x2:
                    slope = 'inf'
                else:
                    slope = (y2-y1)*1.0/(x2-x1)
                if slope not in dic:
                    dic[slope] = 1
                else:
                    dic[slope] += 1
            ans = max(ans, max(dic.values())+samePointsNum+1)
        return ans
# test the solution
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(Solution().maxPoints(points))

points = [[1,1],[2,2],[3,3]]
print(Solution().maxPoints(points))