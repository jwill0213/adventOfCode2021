from os import path


def part1(lines):
    NUM_STEPS = 10
    template = lines[0]

    pairs = {p.split(' -> ')[0]: p.split(' -> ')[1] for p in lines[2:]}

    for step in range(1, NUM_STEPS+1):
        newTemplate = []
        for i in range(len(template)-1):
            currPair = template[i] + template[i+1]
            if currPair in pairs:
                newTemplate.extend(
                    [template[i], pairs[currPair], template[i+1]])
            else:
                newTemplate.append(currPair)
        print("\nSTEP", step, "\n")
        # print("".join(newTemplate))
        template = newTemplate[:]

    print(step, len(template))


def part2(lines):
    pass


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    print("\n----- Part 1 -----\n")
    part1(lines)
    print("\n----- Part 2 -----\n")
    part2(lines)
