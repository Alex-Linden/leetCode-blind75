"""Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            print("base case")
            return []

        res = matrix.pop(0)
        print("top")
        if matrix and matrix[0]:
            print("right")
            for row in matrix:
                res.append(row.pop())
        if len(matrix) > 0:
            print("bottom")
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            print("left", matrix)
            for i in range(len(matrix) - 1, -1, -1):
                res.append(matrix[i].pop(0))
        print(res)
        res += self.spiralOrder(matrix)

        return res
