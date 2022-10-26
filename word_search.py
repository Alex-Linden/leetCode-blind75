"""Write an algorithm to find if the given word occurs in the grid
on a row or a column, forward or backwards.

 Input
The first line of input consists of two integers-
grid_ row and grid col, representing the
number of rows (N) and the number of
columns (M) of the letter grid, respectively.
The next M lines consist of N space-separated
characters representing the letters of the grid.
The next line consists of an integer- word size,
representing the number of words to be
searched from the given grid (K).
The last line consists of K space-separated
strings representing the words to search for in
the grid.
Output
Print K space-separated strings consisting of
"Yes" if the word is present in the grid or "No"
if the word is not present in the grid.
Note
All the inputs are case-sensitive, meaning "a"
and "A" are considered as two different
characters.
Example
Input:
33
CAT
IDO
NOM
4
CAT TOM ADO MOM
Output:
Yes Yes Yes No
Explanation:
From the given words "CAT" is found at the
first row, "TOM" is found at last column,
"ADO" is found at the middle column, but
"MOM" is not found anywhere in the grid.
So, the output is ["Yes", "Yes", "Yes" "No"].
"""


def word_search(grid, words):
    row, col = 0, 0

    res = []

    for word in words:
        word_not_found = True
        while row < len(grid) and word_not_found:
            while col < len(grid[0]):
                if grid[row][col] == word[0]:
                    if has_word(grid, word, [row, col]):
                        res.append("Yes")
                        word_not_found = False
                elif grid[row][col] == word[-1]:
                    if has_word(grid, word[::-1], [row, col]):
                        res.append("Yes")
                        word_not_found = False

                col += 1

            row += 1
            col = 0

        if word_not_found:
            res.append("No")

        row, col = 0, 0
        print(res)

    return res


def has_word(grid, word, position):
    row, col = position[0], position[1]
    i = 0

    horiz_word = ""

    # iterate through a row and check if word is there
    while  col < len(grid[0]):
        if grid[row][col] == word[i]:
            horiz_word += grid[row][col]
        else:
            break

        col += 1
        i += 1

    if horiz_word == word:
        return True

    # reset i and col
    i = 0
    col = position[1]
    # initialize word for vertical comparison
    vert_word = ""

    while row < len(grid):
        if grid[row][col] == word[i]:
            vert_word += grid[row][col]
            print(vert_word)
        else:
            return False

        row += 1
        i += 1

    return vert_word == word



# [["C", "A", "T"],
# ['I', 'D', 'O'],
# ['N', 'O', 'M']]

# ['CAT', 'TOM', 'ADO', 'MOM']




# len(grid[0]) - col >= len(word) - i and i < len(word):



# len(grid) - row >= len(word) - i and i < len(word):