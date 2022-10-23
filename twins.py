"""
Question
Ray, Shiv and Ansh are conducting a survey
for a group of people. The survey is only
meant for twins but there are certain people
who are not twins and wanting to take part in
the survey.
Write an algorithm to help them identify the
person from the given input who is not a twin.
Input
The first line of input consists of an integer-
inputArr size, representing the number of
entries in the array (N).
The next line consists of N space-separated
integer elements in the array.
Output
Print the smallest value of the person who is
not a twin from the given array of elements.
Note
If everyone present is a twin, then return -1.
Examples
Example 1:
Input:
7
1123344
Output:
2
Explanation:
In the given array of element, only non-twin
element is '2'.
So, the output is 2
Example 2:
Input:
4
1122
Output:
-1
Explanation:
Given array of element contain all the twin
elements.
So, the output is -1."""

def find_twins(arr):
    """ return lowest num that is not a twin or -1

    >>> find_twins([1,1,2,2])
    -1

    >>> find_twins([1,1,2,3,3,4,4])
    2
    """

    arr.sort()

    i = 0

    while i < len(arr):
        if arr[i] == arr[i + 1]:
            i += 2
        else:
            return arr[i]

    return -1