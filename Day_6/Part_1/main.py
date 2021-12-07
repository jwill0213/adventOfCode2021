TOTAL_DAYS = 80
SPAWN_RATE = 6  # includes 0
INITIAL_DELAY = 2


def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    fishList = [int(f) for f in lines[0].split(',')]

    for day in range(TOTAL_DAYS):
        newFish = []
        for f in range(len(fishList)):
            fish = fishList[f]
            if fish == 0:
                newFish.append(SPAWN_RATE + INITIAL_DELAY)
                fish = SPAWN_RATE
            else:
                fish -= 1
            fishList[f] = fish
        fishList.extend(newFish[:])

    print(f"Total fish {len(fishList)}")


if __name__ == "__main__":
    main()
