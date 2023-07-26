def main(s):
    chars = ['dream', 'dreamer', 'erase', 'eraser']
    while len(s) >= 5:
        isMatched = False
        for char in chars:
            i = s.rfind(char)
            if len(s)- i != len(char) or i == -1:
                continue            
            elif i == 0:
                return 'YES'
            else:
                s = s[:i]
                isMatched = True
                break
            
        if not isMatched:
            return 'NO'
    return 'NO'

s = input()

print(main(s))
