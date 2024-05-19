#!/usr/bin/python3
'''The N queens problem.
'''
import sys


def printSolution(solutions):
    '''Print the solutions'''
    for solution in solutions:
        print(solution)


def isSafe(solution, row, col):
    '''Check if a queen can be placed on board[row][col]'''
    for i in range(col):
        if solution[i][1] == row or \
           solution[i][0] + solution[i][1] == col + row or \
           solution[i][0] - solution[i][1] == col - row:
            return False
    return True


def solveNQueens(N, solution, solutions, col=0):
    '''Use backtracking to find all solutions'''
    if col == N:
        solutions.append(solution.copy())
        return

    for row in range(N):
        if isSafe(solution, row, col):
            solution[col] = [col, row]
            solveNQueens(N, solution, solutions, col + 1)
            solution[col] = [-1, -1]


def main():
    '''Main function'''
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    solution = [[-1, -1] for _ in range(N)]
    solutions = []

    solveNQueens(N, solution, solutions)

    printSolution(solutions)


if __name__ == '__main__':
    main()
