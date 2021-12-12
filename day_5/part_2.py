class Line:
    HOR = 0
    VER = 1
    DIA = 2
    def __init__(self, x1, y1, x2, y2):
        self.x1 = min(x1, x2)
        self.y1 = min(y1, y2)
        self.x2 = max(x1, x2)
        self.y2 = max(y1, y2)
        self.dir = Line.HOR
        if self.x1 == self.x2:
            self.dir = Line.VER
        elif self.x1 != self.x2 and self.y1 != self.y2:
            self.dir = Line.DIA
    
    def get_intersections(self, line):
        # Check straight lines
        if self.dir == line.dir and (self.dir ==  Line.HOR or self.dir == Line.VER):
            a1, a2, b1, b2 = 0, 0, 0, 0
            if self.dir == Line.HOR:
                if self.y1 != line.y1:
                    return []
                a1, a2 = self.x1, self.x2
                b1, b2 = line.x1, line.x2
            else:
                if self.x1 != line.x1:
                    return []
                a1, a2 = self.y1, self.y2
                b1, b2 = line.y1, line.y2
            if (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a1 <= b2) or (a2 >= b1 and a2 <= b2):
                start = max(a1, b1)
                end = min(a2, b2)
                if self.dir == Line.HOR:
                    return [(x, self.y1) for x in range(start, end+1)]
                else:
                    return [(self.x1, y) for y in range(start, end+1)]
        elif self.dir == Line.HOR:
            if self.x1 <= line.x1 and self.x2 >= line.x1 and self.y1 >= line.y1 and self.y1 <= line.y2:
                return [(line.x1, self.y1)]
        else:
            if self.y1 <= line.y1 and self.y2 >= line.y1 and self.x1 >= line.x1 and self.x1 <= line.x2:
                return [(self.x1, line.y1)]
        return []

def Run(data):
    data = (x.split(' -> ') for x in data.splitlines())
    data = ((x.split(','), y.split(',')) for x, y in data)
    lines = []
    for item in data:
        line = Line(int(item[0][0]), int(item[0][1]), int(item[1][0]), int(item[1][1]))
        lines.append(line)

    intersections = set()
    count = 0
    for i, line in enumerate(lines[:-1]):
        for check_line in lines[i + 1:]:
            inters = line.get_intersections(check_line)
            for inter in inters:
                if inter not in intersections:
                    count += 1
                    intersections.add(inter)
    return str(count)

if __name__ == '__main__':
    result = Run('''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2''')
    aoc = '5'
    print(f'AoC: {aoc}\nYou: {result}{"  ☑" if result == aoc else "  ☒"}')