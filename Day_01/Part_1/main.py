def main():
    total_increases = 0
    with open('input.txt') as f:
        prev = None
        for line in f:
            curr = line.rstrip()
            if prev is None:
                print(f'{curr} (N/A - no previous measurement)')
            elif int(curr) > int(prev):
                print(f'{curr} (increased)')
                total_increases += 1
            elif int(prev) > int(curr):
                print(f'{curr} (decreased)')
            else:
                print(f'{curr} (no change)')
            prev = curr
    print(
        f'There are {total_increases} measurements that are larger than the previous measurement.')


if __name__ == "__main__":
    main()
