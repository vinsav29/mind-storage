def solution(n, a):
    nums = list(range(1, n+1))

    for id1 in range(0, n, 2):
        id2 = id1 + 1

        for i in range(id2 + 1, n):
            if abs(a[i] - a[id1]) < abs(a[id2] - a[id1]):
                id2 = i

        a.insert(id1 + 1, a.pop(id2))
        nums.insert(id1 + 1, nums.pop(id2))
        print(nums[id1], nums[id1 + 1])


t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solution(n, a)
