

def solution(n, p):
    pages = p.split(",")
    printed = set()
    for page in pages:
        if "-" in page:
            start, stop = map(int, page.split("-"))
            for i in range(start, stop + 1):
                printed.add(i)
        else:
            printed.add(int(page))

    # res = []
    prevP = 0
    # seq = [1, 0]
    seq = False
    res = []
    for i in range(1, n + 1):
        #
        # def add():
        #     if seq[0] == seq[1]:
        #         res.append(str(seq[0]))
        #     else:
        #         res.append(f"{str(seq[0])}-{str(seq[1])}")
        #     return res
        #
        #
        # if i not in printed:
        #     if i - 1 == seq[1]:
        #         seq[1] = i
        #     else:
        #         add()
        #         seq = [i, i]
        #     if i == n:
        #         add()
        if i not in printed:
            res.append(i)
            # if i - 1 == prevP:
            #     if res == "":
            #         res += f"{str(i)}"
            #     prevP = i
            #     seq = True
            # else:
            #     if res:
            #         if seq:
            #             # end of seq, next page
            #             res += f"-{str(prevP)},{str(i)}"
            #         else:
            #             res += f",{str(i)}"
            #     else:
            #         # first symbol
            #         res += f"{str(i)}"
            #     seq = False
        ress = f"{res}"
        for i in res:
            ress += str(i)
    return

t = int(input())
for _ in range(t):
    k = int(input())
    p = input()
    print(solution(k, p))
