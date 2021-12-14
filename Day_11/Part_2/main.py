def main():
    with open('input.txt') as f:
        octopuses = [[int(num) for num in line.rstrip()]
                     for line in f.readlines()]

    maxIndex = (len(octopuses[0]) - 1, len(octopuses) - 1)
    totalOctopuses = len(octopuses[0]) * len(octopuses)
    numFlashes = 0

    allFlashed = False
    step = 1
    while not allFlashed:
        flashesThisStep = 0
        # Incerement enegery of all indexes by 1
        for y in range(len(octopuses)):
            for x in range(len(octopuses[0])):
                octopuses[y][x] += 1

        # "Flash" all indexes that are at 9 or greater
        flashLoop = True
        while flashLoop:
            flashLoop = False
            for y in range(len(octopuses)):
                for x in range(len(octopuses[0])):
                    if octopuses[y][x] != '*' and octopuses[y][x] > 9:
                        octopuses[y][x] = '*'
                        flashesThisStep += 1
                        incrementList = findSurroundingPoints(
                            (x, y), maxIndex)
                        for point in incrementList:
                            x, y = point
                            if octopuses[y][x] != '*':
                                octopuses[y][x] += 1
                                flashLoop = True

        # Set all flashed octopuses, *,  to 0
        for y in range(len(octopuses)):
            for x in range(len(octopuses[0])):
                if octopuses[y][x] == '*':
                    octopuses[y][x] = 0

        print(step, flashesThisStep, totalOctopuses)
        if flashesThisStep == totalOctopuses:
            allFlashed = True
            print("All Octopuses flashed at step", step)
        else:
            numFlashes += flashesThisStep
        step += 1


def findSurroundingPoints(currPoint, maxIndex):
    x, y = currPoint
    newPoints = []

    # get left point
    if not x - 1 < 0:
        newPoints.append((x-1, y))
    # get right point
    if not x + 1 > maxIndex[0]:
        newPoints.append((x+1, y))
    # get up point
    if not y - 1 < 0:
        newPoints.append((x, y-1))
    # get down point
    if not y + 1 > maxIndex[1]:
        newPoints.append((x, y+1))

    # get top left point
    if not x - 1 < 0 and not y - 1 < 0:
        newPoints.append((x-1, y-1))
    # get top right point
    if not x + 1 > maxIndex[0] and not y - 1 < 0:
        newPoints.append((x+1, y-1))
    # get bottom left point
    if not x - 1 < 0 and not y + 1 > maxIndex[1]:
        newPoints.append((x-1, y+1))
    # get bottom right point
    if not x + 1 > maxIndex[0] and not y + 1 > maxIndex[1]:
        newPoints.append((x+1, y+1))

    return newPoints


if __name__ == "__main__":
    main()
