import numpy as np

def part1(p2):
    counter = 0
    for ds in p2:
        for d in ds:
            if len(d) in [2, 4, 3, 7]:
                counter += 1
    return counter


def part2(p1, p2):
    counter = 0
    for i in range(len(p1)):
        # the segments for digits 1 and 4 
        segment_dict = {len(d): set(d) for d in p1[i] if len(d) in [2, 4]}

        outnum = ""
        for d in p2[i]:
            l = len(d)
            if l == 2: outnum += "1"
            elif l == 4: outnum += "4"
            elif l == 3: outnum += "7"
            elif l == 7: outnum += "8"
            elif l == 5: 
                segments = set(d)
                common_segments_1 = segments & segment_dict[2]
                common_segments_4 = segments & segment_dict[4]
                if len(common_segments_1) == 2: outnum += "3"
                elif len(common_segments_4) == 2: outnum += "2"
                else: outnum += "5"
            else:
                segments = set(d)
                common_segments_1 = segments & segment_dict[2]
                common_segments_4 = segments & segment_dict[4]
                if len(common_segments_1) == 1: outnum += "6"
                elif len(common_segments_4) == 4: outnum += "9"
                else: outnum += "0"
        counter += int(outnum)
    return counter


def parsefile(infile):
    p1 = []
    p2 = []
    for line in open(infile):
        line = line.strip()
        parts = line.split('|')
        p1.append(parts[0].strip().split())
        p2.append(parts[1].strip().split())
    return p1, p2

def run():
    p1, p2 = parsefile('day8.input')
    print(f'Part 1: {part1(p2)}')
    print(f'Part 2: {part2(p1, p2)}')
    
if __name__ == '__main__':
    run()