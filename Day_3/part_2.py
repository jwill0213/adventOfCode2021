def main():
    lines = []
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    oxygenRatingList = []
    co2ScrubberList = []
    onesList = []
    zerosList = []

    for line in lines:
        if line[0] == '1':
            onesList.append(line)
        else:
            zerosList.append(line)

    if len(onesList) >= len(zerosList):
        oxygenRatingList = onesList[:]
        co2ScrubberList = zerosList[:]
    else:
        oxygenRatingList = zerosList[:]
        co2ScrubberList = onesList[:]

    for col in range(1, len(oxygenRatingList[0])):
        if len(oxygenRatingList) > 1:
            onesList = []
            zerosList = []
            for rating in oxygenRatingList:
                if rating[col] == '1':
                    onesList.append(rating)
                else:
                    zerosList.append(rating)

            if len(onesList) >= len(zerosList):
                oxygenRatingList = onesList[:]
            else:
                oxygenRatingList = zerosList[:]

        if len(co2ScrubberList) > 1:
            onesList = []
            zerosList = []
            for rating in co2ScrubberList:
                if rating[col] == '1':
                    onesList.append(rating)
                else:
                    zerosList.append(rating)

            if len(onesList) >= len(zerosList):
                co2ScrubberList = zerosList[:]
            else:
                co2ScrubberList = onesList[:]

        if len(oxygenRatingList) == 1 and len(co2ScrubberList) == 1:
            break

    oxygenRating = int(oxygenRatingList[0], base=2)
    co2ScrubberRating = int(co2ScrubberList[0], base=2)
    print(
        f'Oxygen Rating: {oxygenRating}\nCO2 Rating: {co2ScrubberRating}\nLife Support Rating: {oxygenRating * co2ScrubberRating}')


if __name__ == "__main__":
    main()
