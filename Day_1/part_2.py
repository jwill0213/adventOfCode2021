def main():
    total_increases = 0
    with open('input.txt') as f:
        lines = [int(line.rstrip()) for line in f.readlines()]
        currOffset = 0
        while currOffset < len(lines):
            if currOffset == 0:
                print(
                    f'{sum(lines[currOffset:currOffset + 3])} (N/A - no previous sum)')
                currOffset += 1
                continue
            currSum = sum(lines[currOffset:currOffset + 3])
            prevSum = sum(lines[currOffset-1:currOffset+2])
            if currSum > prevSum:
                print(f'{currSum} (increased)')
                total_increases += 1
            elif currSum < prevSum:
                print(f'{currSum} (decreased)')
            else:
                print(f'{currSum} (no change)')
            currOffset += 1
    print(
        f'There are {total_increases} measurements that are larger than the previous measurement.')


if __name__ == "__main__":
    main()
