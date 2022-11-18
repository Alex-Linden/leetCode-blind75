"""write an algorithm which finds out elements which are largest
in a row and smallest in a column in a matrix

The first line of input consists of two space-
separated integers-
matrix row and matrix col, representing the
number of rows in the matrix (N) and the
number of columns in the matrix (M),
respectively.
The next M lines consist of N space-separated
integers representing the elements of the
matrix.
Output
Print a number which is largest in a row and
smallest in a column in the given matrix. If no
element is found print -1'.
Constraints
1 < N, M ≤ 1000
Note
Each number in the matrix is a non-negative
integer.
Example
Input:
22
12
34
Output:
2
Explanation:
The number 2 at index (0,1) is the largest in its
row and smallest in its column.
So, the output is 2."""


def smallest_largest(grid):
    """
    >>> smallest_largest([[1, 2], [3, 4]])
    [2]
     """
    smallest_per_col = [None] * len(grid[0])

    res = []

    for row in grid:
        largest = row[0]
        i_of_lrg = 0

        for i in range(len(row)):
            if largest < row[i]:
                largest = row[i]
                i_of_lrg = i

        if (smallest_per_col[i_of_lrg] is not None and
                largest == smallest_per_col[i_of_lrg]):
            res.append(largest)
        elif smallest_per_col[i_of_lrg] is None:
            smallest = largest
            for j in range(len(grid)):
                smallest = min(smallest, grid[j][i_of_lrg])
            smallest_per_col[i_of_lrg] = smallest
            if smallest == largest:
                res.append(largest)

    return res
