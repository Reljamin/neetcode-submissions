class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        answerCol = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        answerSquare = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        

        for row in range(len(board)):
            curRowAnswer = set()
            for column in range(len(board[0])):
                
                current_number = board[row][column]

                if current_number == ".":
                    continue
                
                square_index = ((row // 3) * 3 + (column // 3))

                if current_number in (curRowAnswer | answerCol[column] | answerSquare[square_index]):
                    return False
                
                curRowAnswer.add(current_number)
                answerCol[column].add(current_number)
                answerSquare[square_index].add(current_number)
                
                
        return True

                