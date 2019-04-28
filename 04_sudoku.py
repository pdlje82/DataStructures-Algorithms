correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 1]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

# Define a function check_sudoku() here:
def check_list(list1):
    d = {}
    check_list = list(range(1, len(list1) + 1))
    for e in list1:
        if e not in d.keys():
            if isinstance(e, int):
                d[e] = 1
            else:
                 return False
        else:
            return False
    for key in d:
        if key not in check_list:
            return False


def check_sudoku(square):
     for i in range(len(square[0])):
         print(square[i], [row[i] for row in square])
         if check_list(square[i]) is False or check_list([row[i] for row in square]) is False:
             return False
     return True

#print(correct[2])
#print(check_list(correct[2]))



print(check_sudoku(incorrect))

# # >>> False
#
print(check_sudoku(correct))
# # >>> True
#
# print(check_sudoku(incorrect2))
# # >>> False
#
#print(check_sudoku(incorrect3))
# # >>> False
#
# print(check_sudoku(incorrect4))
# # >>> False
#
# print(check_sudoku(incorrect5))
# # >>> False
#
#
