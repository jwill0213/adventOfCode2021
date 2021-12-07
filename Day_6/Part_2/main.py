TOTAL_DAYS = 256
SPAWN_RATE = 6  # includes 0
INITIAL_DELAY = 2


def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    fishList = [int(f) for f in lines[0].split(',')]
    fishDict = {}

    for f in fishList:
        if f in fishDict:
            fishDict[f] += 1
        else:
            fishDict[f] = 1

    for day in range(TOTAL_DAYS):
        newFish = {}
        for f, num in fishDict.items():
            if f == 0:
                # Set new fish to spawn + initial delay
                if SPAWN_RATE + INITIAL_DELAY in newFish:
                    newFish[SPAWN_RATE + INITIAL_DELAY] += num
                else:
                    newFish[SPAWN_RATE + INITIAL_DELAY] = num

                # set exisiting fish to spawn valuer
                if SPAWN_RATE in newFish:
                    newFish[SPAWN_RATE] += num
                else:
                    newFish[SPAWN_RATE] = num
            else:
                if f-1 in newFish:
                    newFish[f-1] += num
                else:
                    newFish[f-1] = num
        fishDict = newFish

    print(f"Total fish {sum(fishDict.values())}")


if __name__ == "__main__":
    main()
