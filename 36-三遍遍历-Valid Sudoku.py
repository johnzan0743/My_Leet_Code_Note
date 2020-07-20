class Solution:
    def isValidSudoku(self, board):
        A = set()
        for i in range(9):
            for item in board[i]:  # row
                if item == '.':
                    continue
                else:
                    if item not in A:
                        A.add(item)
                    else:
                        #self.flag = 1
                        return False
            A = set() # 重置set
        for i in range(9):
            for item in [x[i] for x in board]:
                if item == '.':
                    continue
                else:
                    if item not in A:
                        A.add(item)
                    else:
                        #self.flag = 1
                        return False
            A = set()

        def box_of_nine(board,a,b,initial_set):
            initial_set = set()
            for p in range(3):
                for q in range(3):
                    if board[a+p][b+q] == '.':
                        continue
                    else:
                        if board[a+p][b+q] not in initial_set:
                            initial_set.add(board[a+p][b+q])  
                        else:
                            return False
                               
        a = [0,3,6]
        b = [0,3,6]
        for i in a:
            for j in b:
                Q = box_of_nine(board,i,j,set()) 
                if Q == False:
                    return False
        return True



class Solution:
    def __init__(self):
        self.flag = 0
    def isValidSudoku(self, board):
        A = set()
        for i in range(9):
            for item in board[i]:  # row
                if item == '.':
                    continue
                else:
                    if item not in A:
                        A.add(item)
                    else:
                        #self.flag = 1
                        return False
            A = set() # 重置set
        for i in range(9):
            for item in [x[i] for x in board]:
                if item == '.':
                    continue
                else:
                    if item not in A:
                        A.add(item)
                    else:
                        #self.flag = 1
                        return False
            A = set()

        def box_of_nine(board,a,b,initial_set):
            initial_set = set()
            for p in range(3):
                for q in range(3):
                    if board[a+p][b+q] == '.':
                        continue
                    else:
                        if board[a+p][b+q] not in initial_set:
                            initial_set.add(board[a+p][b+q])  
                        else:
                            self.flag = 1
                               
        a = [0,3,6]
        b = [0,3,6]
        for i in a:
            for j in b:
                box_of_nine(board,i,j,set())
        return self.flag == 0