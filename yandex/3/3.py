def solution(n, nums, k, kums):
    if n == 0:
        for _ in range(k):
            print(0)
        return

    for kum in kums:
        if kum > nums[-1]:
            print(length)
            continue
        low, high, mid = 0, length, 0
        while low <= high:

            mid = low + (high - low) // 2

            if nums[mid] == kum:
                break

            elif nums[mid] < kum:
                low = mid + 1

            else:
                high = mid - 1
        if kum > nums[mid]:
            mid += 1
        print(mid)

f = open("input.txt")
lines = f.read().splitlines()
f.close()

n = int(lines[0])
nums = []
prev = -1
for x in sorted(map(int, lines[1].split())):
    if x != prev:
        nums.append(x)
        prev = x
# print(nums)

k = int(lines[2])
if k != 0:
    kums = list(map(int, lines[3].split()))
    length = len(nums)

    solution(n, nums, k, kums)