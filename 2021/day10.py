import numpy as np

def part1(strings):
    penalties = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    reverse_lookup = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    total_penalties = 0
    for s in strings:
        stack = []
        for c in s:
            if c in penalties.keys():
                if stack[-1] != reverse_lookup[c]:
                    total_penalties += penalties[c]
                    break
                stack.pop()
            else:
                stack.append(c)
    return total_penalties
            
def part2(strings):
    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    reverse_lookup = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    lookup = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    string_scores = []
    for s in strings:
        score = 0
        stack = []
        penalty = False
        for c in s.strip():
            if c in scores.keys():
                if stack[-1] != reverse_lookup[c]:
                    penalty = True
                    break
                stack.pop()
            else:
                stack.append(c)
        if not penalty:
            while stack:
                c = stack.pop()
                if c in lookup.keys():
                    score *= 5
                    score += scores[lookup[c]]
            string_scores.append(score)
    string_scores = sorted(string_scores)    
    return string_scores[len(string_scores)//2]

def run():
    strings = open('day10.input').readlines()
    print(f'Part 1: {part1(strings)}')
    print(f'Part 2: {part2(strings)}')
    
if __name__ == '__main__':
    run()