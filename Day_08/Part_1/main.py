def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    numOfVals = 0

    for line in lines:
        # Ignore the unique pattern for part 1
        _, outputVal = line.split(' | ')

        for val in outputVal.split():
            if len(val) in [2, 3, 4, 7]:
                numOfVals += 1

    print(f"Numer of appearences: {numOfVals}")


if __name__ == "__main__":
    main()
