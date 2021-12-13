SCORE_MAP = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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

    score = 0
    currentChunk = []
    for line in lines:
        for c in line:
            if c in chunkPairs.keys():
                # open chunck so append to current chunk
                currentChunk.append(c)
            else:
                lastChunkOpen = currentChunk.pop()
                if chunkPairs[lastChunkOpen] != c:
                    # invalid character
                    score += SCORE_MAP[c]
                    break

    print(f"Syntax Error Score {score}")


if __name__ == "__main__":
    main()
