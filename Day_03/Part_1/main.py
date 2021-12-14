def main():
    lines = []
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    gamma = ''
    epsilon = ''

    for col in range(len(lines[0])):
        num_ones = 0
        num_zeros = 0
        colVals = [line[col] for line in lines]
        for val in colVals:
            if val == '1':
                num_ones += 1
            elif val == '0':
                num_zeros += 1
        if num_ones > num_zeros:
            gamma += '1'
            epsilon += '0'
        elif num_zeros > num_ones:
            gamma += '0'
            epsilon += '1'
    epsilonRate = int(epsilon, base=2)
    gammaRate = int(gamma, base=2)
    print(
        f'Epislon: {epsilonRate}\nGamma: {gammaRate}\nPower Consumption: {epsilonRate * gammaRate}')


if __name__ == "__main__":
    main()
