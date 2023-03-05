
def solution(max_replaces, s):
    maxBeauty = 0
    length = len(s)
    if length == 1:
        return 1

    order = ord("a")
    while order <= ord("z"):
        letter = chr(order)

        right = 0
        replace = max_replaces
        for left in range(0, length - 1):
            if left > 0 and s[left - 1] != letter:
                replace += 1    # каждый сдвиг левого указателя с буквы не == letter дает одну доп замену

            while right < length:
                if s[right] != letter:
                    if replace == 0:
                        break
                    replace -= 1
                right += 1
            maxBeauty = max(maxBeauty, right - left)

        order += 1

    return maxBeauty

f = open("input.txt")
lines = f.read().splitlines()
f.close()

k = int(lines[0])
s = lines[1]
print(solution(k,s))

# import collections
#
#
#
# # k = int(input())
# # s = input()
# maxf = i = 0
# count = collections.Counter()
# for j in range(len(s)):
#     print(j)
#     count[s[j]] += 1
#     maxf = max(maxf, count[s[j]])
#     if j - i + 1 > maxf + k:
#         count[s[i]] -= 1
#         i += 1
# print(len(s) - i)


