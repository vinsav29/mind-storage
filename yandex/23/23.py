# def sol(n):
#     step = 0
#     dp = [1]
#     prev = [-1]
#     start, stop = 0, 1
#     hashNums = set()
#     while n not in dp[start:stop]:
#
#         inc = 0
#         for i in range(start, stop):
#             for x in (dp[i] + 1, dp[i]*2, dp[i]*3):
#                 if x not in hashNums:
#                     hashNums.add(x)
#                     dp.append(x)
#                     prev.append(i)
#                     inc += 1
#
#                     if dp[-1] == n:
#                         break
#             if dp[-1] == n:
#                 break
#
#         start = stop
#         stop += inc
#
#         step += 1
#         # if 1 in :
#         #     break
#
#     print(step)
#
#     res = [str(dp[-1])]
#     idx = prev[-1]
#     while idx != -1:
#         res.append(str(dp[idx]))
#         idx = prev[idx]
#     print(" ".join(res[::-1]))

def sol(n):
    if n == 1:
        print(0)
        print(1)
        return
    if n in (2, 3):
        print(1)
        print(f"1 {n}")
        return
    prev = list(zip([0, 0, 1, 1], [-1, -1, 1, 1])) + [(0, 0)]*(n - 3)

    for i in range(4, n + 1):
        vars = [(prev[i-1][0], i-1)]
        if not i % 3:
            vars.append((prev[i//3][0], i//3))
        if not i % 2:
            vars.append((prev[i // 2][0], i // 2))
        minDp = min(vars)
        prev[i] = minDp[0]+1, minDp[1]


    res = [str(n)]
    idx = -1
    count = 0
    while idx != 1:
        res.append(str(prev[idx][1]))
        idx = prev[idx][1]
        count += 1
    print(count)
    print(" ".join(res[::-1]))


n = int(input())
sol(n)


# def main():
#     n = int(input())
#     dp = [0, 1, 1, 1] + [0]*(n - 3)
#     for i in range(4, n + 1):
#         if not i % 3 and not i % 2:
#             dp[i] = min([dp[i // 2], dp[i // 3], dp[i - 1]]) + 1
#         elif not i % 3:
#             dp[i] = min(dp[i // 3], dp[i - 1]) + 1
#         elif not i % 2:
#             dp[i] = min(dp[i // 2], dp[i - 1]) + 1
#         else:
#             dp[i] = dp[i - 1] + 1
#     ans = [n]
#     pointer = n
#     while pointer != 1:
#         if pointer % 2 and pointer % 3:
#             pointer -= 1
#         elif not pointer % 2 and pointer % 3:
#             if dp[pointer // 2] <= dp[pointer - 1]:
#                 pointer //= 2
#             else:
#                 pointer -= 1
#         elif not pointer % 3 and pointer % 2:
#             if dp[pointer // 3] <= dp[pointer - 1]:
#                 pointer //= 3
#             else:
#                 pointer -= 1
#         else:
#             if dp[pointer // 3] <= dp[pointer // 2] and dp[pointer // 3] <= dp[pointer - 1]:
#                 pointer //= 3
#             elif dp[pointer // 2] <= dp[pointer // 3] and dp[pointer // 2] <= dp[pointer - 1]:
#                 pointer //= 2
#             else: pointer -= 1
#         ans.append(pointer)
#     print(len(ans) - 1)
#     print(" ".join(str(k) for k in ans[::-1]))
#
# main()
