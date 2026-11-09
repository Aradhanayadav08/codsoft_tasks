"""Tic-Tac-Toe AI using Minimax Algorithm.
Run: python tic_tac_toe.py
"""
import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '


def print_board(board):
    print('\n')
    for i in range(3):
        row = board[3*i:3*i+3]
        print(' | '.join(row))
        if i < 2:
            print('--+---+--')
    print('\n')


def winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    if EMPTY not in board:
        return 'Draw'
    return None


def minimax(board, is_maximizing):
    result = winner(board)
    if result == AI:
        return 1
    if result == HUMAN:
        return -1
    if result == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, False)
                board[i] = EMPTY
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = EMPTY
                best_score = min(best_score, score)
        return best_score


def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move


def main():
    board = [EMPTY] * 9
    print('Tic-Tac-Toe AI using Minimax')
    print('You are X. Enter position 1-9.')
    while True:
        print_board([str(i+1) if v == EMPTY else v for i, v in enumerate(board)])
        try:
            pos = int(input('Your move: ')) - 1
            if pos not in range(9) or board[pos] != EMPTY:
                print('Invalid move. Try again.')
                continue
        except ValueError:
            print('Enter a valid number.')
            continue

        board[pos] = HUMAN
        if winner(board):
            break

        ai_pos = best_move(board)
        board[ai_pos] = AI
        print(f'AI placed O at position {ai_pos + 1}')
        if winner(board):
            break

    print_board(board)
    result = winner(board)
    if result == 'Draw':
        print('Game Draw!')
    else:
        print(f'{result} wins!')


if __name__ == '__main__':
    main()
