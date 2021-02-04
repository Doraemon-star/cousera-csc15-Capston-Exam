'''
"Pick-A-Number" is a game in which the board consists of a list of numbers. 
On a player's turn, that player may pick a number on either end of the list. 
Turns alternate. When the list is exhausted, the winner is the player with the 
highest sum of the numbers they picked.

For example, consider the following game board:

3, 5, 2, 1

Players P1 and P2 play optimally as follows:

P1 picks 1, leaving 3, 5, 2
P2 picks 3, leaving 5, 2
P1 picks 5, leaving 2
P2 picks 2
P1 then wins 6 to 5.
Write a recursive function, pick_a_number(board) that takes a list representing 
the game board and returns a tuple that is the score of the game if both players 
play optimally. Here, optimal play means that the player maximizes his/her final
score. The returned tuple should be ordered with the current player's score first 
and the other player's score second.


'''
def a(board):
    if len(board)==1:
        return (0,board[0])
    elif len(board) == 2:
        return (max(board), min(board))
    elif len(board) == 3:
        p1_1 = max(board[0], board[-1])
        board.remove(p1_1)
        p2 = max(board)
        p1 = p1_1 + min(board)
        return (p2, p1)
    else:
        if len(board) % 2 ==0:
            p1_lt = board[0] + a(board[1:])[0]
            p1_rt = board[-1] + a(board[:-1])[0]
            p1 = max(p1_lt, p1_rt)
            return (p1, sum(board)-p1)
        else:
            p1_lt = board[0] + a(board[1:])[1]
            p1_rt = board[-1] + a(board[:-1])[1]
            p1 = max(p1_lt, p1_rt)
            return (sum(board)-p1, p1)
        
        
print a([12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1])
        
    
