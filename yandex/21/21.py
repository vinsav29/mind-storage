

def solution(n):
    x = 1   # all prev 1
    y = 0   # doubled prev 1
    sum = 2
    step = 1
    while step < n:
        sum, x, y = sum*2-y, sum-y, x-y

        step += 1
    return sum
n = int(input())

print(solution(n))