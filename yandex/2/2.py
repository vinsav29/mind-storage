f = open("input.txt")
lines = f.read().splitlines()
f.close()

k = int(lines[0])
s = lines[1]

# maxBeauty = 0
# length = len(s)
# for i in range(0, length - 2):
#     j = i + 1
#     replace = 0
#     while j < length:
#         if s[j] != s[i]:
#             replace += 1
#             if replace > k:
#                 break
#         j += 1
#     maxBeauty = max(maxBeauty, j-i)
# print(maxBeauty)
import collections



# k = int(input())
# s = input()
maxf = i = 0
count = collections.Counter()
for j in range(len(s)):
    print(j)
    count[s[j]] += 1
    maxf = max(maxf, count[s[j]])
    if j - i + 1 > maxf + k:
        count[s[i]] -= 1
        i += 1
print(len(s) - i)


