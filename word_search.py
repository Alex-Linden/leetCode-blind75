"""Write an algorithm to find if the given word
occurs in the grid on a row or a column,
forward or backwards.
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




def has_word(grid, word, position):
    x, y = position
    i = 0

    while x < len(word) + x and x < len(grid[0]):


        if not grid[x][y] == word[i]:
            return False

        x += 1
        i += 1

    while y < len(word) + y and :





    return False