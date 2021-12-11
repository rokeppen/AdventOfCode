def read_file(f):
    numbers = f.readline().strip().split(',')
    cards, card = [], []
    for x in f:
        if x.strip() == '':
            if len(card) > 0:
                cards.append(card.copy())
            card = []
        else:
            card.append(x.strip().split())
    if len(card) > 0:
        cards.append(card.copy())
    return numbers, cards


def get_bingo_card(card, numbers):
    for i, number in enumerate(numbers):
        for line in card:
            if number in line:
                index = line.index(number)
                line[index] = ''
                if not any(line) or not any(x[index] for x in card):
                    return i, number, sum(int(x) for y in card for x in filter(None, y))


def get_bingo(f):
    numbers, cards = read_file(open("input.txt"))
    card = f(get_bingo_card(card, numbers) for card in cards)
    return int(card[1]) * card[2]


if __name__ == '__main__':
    print(get_bingo(min))
    print(get_bingo(max))
