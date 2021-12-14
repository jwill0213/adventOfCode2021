def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    lowPoints = []
    maxIndexX = len(lines[0]) - 1
    maxIndexY = len(lines) - 1
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            up = down = left = right = False
            currVal = int(lines[y][x])
            if y == 0 or int(lines[y-1][x]) > currVal:
                up = True
            if x == 0 or int(lines[y][x-1]) > currVal:
                left = True
            if y == maxIndexY or int(lines[y+1][x]) > currVal:
                down = True
            if x == maxIndexX or int(lines[y][x+1]) > currVal:
                right = True

            if up and down and left and right:
                lowPoints.append(currVal)
    print(f"Points: {lowPoints}\nRisk Level: {sum([1+h for h in lowPoints])}")


if __name__ == "__main__":
    main()
