import heapq
# def solution(text):
#     charCounter = {}
#     maxH = 0
#     for c in text:
#         if c not in (" ", "\n"):
#             newCnt = charCounter.get(c, 0) + 1
#             maxH = max(maxH, newCnt)
#             charCounter[c] = newCnt
#     symbols = sorted(charCounter.keys(), key=lambda item: ord(item))
#     for rowIndex in range(maxH, 0, -1):
#         line = []
#         for s in symbols:
#             if charCounter[s] >= rowIndex:
#                 line.append("#")
#             else:
#                 line.append(" ")
#
#         print("".join(line))
#     print("".join(symbols))

def solution():
    charCounter = {}
    maxH = 0
    for c in text:
        if c not in (" ", "\n"):
            newCnt = charCounter.get(c, 0) + 1
            maxH = max(maxH, newCnt)
            charCounter[c] = newCnt
    symbols = sorted(charCounter.keys(), key=lambda item: ord(item))

    res = [" "] * len(symbols)

    heapq.heapify(charCounter)


with open("input.txt") as f:
    text = f.read()
    solution(text)
