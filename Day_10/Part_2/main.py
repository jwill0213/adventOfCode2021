SCORE_MAP = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

chunkPairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    lineScores = []
    for line in lines:
        currentChunk = []
        invalidLine = False
        for c in line:
            if c in chunkPairs.keys():
                # open chunck so append to current chunk
                currentChunk.append(c)
            else:
                lastChunkOpen = currentChunk.pop()
                if chunkPairs[lastChunkOpen] != c:
                    # invalid character ignore the line
                    invalidLine = True
                    break
        if not invalidLine:
            lineSolution = [chunkPairs[c] for c in currentChunk[::-1]]
            lineScore = 0
            for s in lineSolution:
                lineScore *= 5
                lineScore += SCORE_MAP[s]

            print("".join(lineSolution), lineScore)
            lineScores.append(lineScore)

    lineScores.sort()
    print(f"Syntax Error Score {lineScores[int((len(lineScores)-1)/2)]}")


if __name__ == "__main__":
    main()
