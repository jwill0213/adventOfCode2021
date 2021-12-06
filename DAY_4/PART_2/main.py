import re


def main():
    # 0 is moves, 1 is empty line, 2 is start of first board
    boardsStart = 2
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    bingoNums = lines[0].split(',')

    currentBoard = 0
    allBoards = [[]]
    for line in lines[boardsStart:]:
        if line == '':
            currentBoard += 1
            allBoards.append([])
            continue
        allBoards[currentBoard].append(line.strip().split())

    winningBoards = []
    for num in bingoNums:
        for b in range(len(allBoards)):
            if b in [w[2] for w in winningBoards]:
                continue
            board = allBoards[b]
            markNumber(board, num)
            winner = checkForWin(board)
            if winner:
                if b not in winningBoards:
                    winningBoards.append((allBoards[b], int(num), b))
    winningBoard = winningBoards[-1]
    winningSum = findWinningSum(winningBoard[0])
    winningNum = winningBoard[1]
    print(
        f"Winner found!\nBoard Sum:{winningSum}\nNumber: {winningNum}\nFinal Score: {winningSum * winningNum}")


def markNumber(board, num):
    for y in board:
        for x in range(len(y)):
            if y[x] == num:
                y[x] = f'-{num}-'


def checkForWin(board):
    win = None
    # check rows
    for y in range(len(board)):
        unmarkedNums = [x for x in board[y] if not re.search(r'-[0-9]+-', x)]
        if len(unmarkedNums) == 0:
            win = True
            break
    if not win:
        for x in range(len(board[0])):
            unmarkedNum = False
            for y in range(len(board)):
                if not re.search(r'-[0-9]+-', board[y][x]):
                    unmarkedNum = True
                    break
            if not unmarkedNum:
                win = True
                break
    return win


def findWinningSum(board):
    print(board)
    unmarkedNums = []
    for y in range(len(board)):
        unmarkedNums.extend(
            [int(x) for x in board[y] if not re.search(r'-[0-9]+-', x)])
    return sum(unmarkedNums)


if __name__ == "__main__":
    main()
