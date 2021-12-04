class BingoCard:
    def __init__(self):
        self.card = []
        self.called = []

    def addRow(self, row):
        self.card.append(row)
        self.called.append([False] * len(row))
    
    def call(self, number):
        for i, row in enumerate(self.card):
            for j, val in enumerate(row):
                if val == number:
                    self.called[i][j] = True

    def checkBingo(self):
        for i, row in enumerate(self.card):
            col = [x[i] for x in self.card]
            called_col = [x[i] for x in self.called]
            if self.called[i].count(True) == len(row) or called_col.count(True) == len(col):
                return True
        return False

    def sumUnmarked(self):
        result = 0
        for i, row in enumerate(self.card):
            for j, val in enumerate(row):
                if self.called[i][j] == False:
                    result += int(val)
        return result

def Run(data):
    data = iter(data.splitlines())
    called = next(data).split(',')
    next(data) # skip blank line
    
    current_card = BingoCard()
    cards = []
    for line in data:
        if line == '':
            cards.append(current_card)
            current_card = BingoCard()
        else:
            current_card.addRow(line.lstrip().replace('  ', ' ').split(' '))
    else:
        cards.append(current_card)
    
    for num in called:
        for card in cards:
            card.call(num)
            if card.checkBingo():
                return str(card.sumUnmarked() * int(num))
    return None

if __name__ == '__main__':
    result = Run('''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7''')
    aoc = '4512'
    print(f'AoC: {aoc}\nYou: {result}{"  ☑" if result == aoc else "  ☒"}')