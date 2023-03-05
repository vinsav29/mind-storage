
def solution(lines):
    n = int(lines[0])
    k = int(lines[1])
    pet_row = int(lines[2])
    left_right = int(lines[3])

    place = (pet_row-1)*2 + left_right
    var = place // k + 1
    if var == 0:
        var = k
    back_place = place + k
    res_row = n//2 + 2  # more than rows in class
    res_place = n + 1   # more than people
    if back_place <= n:
        res_place = back_place
        res_row = back_place//2 + 1

    front_place = place - k
    if front_place > 0:
        front_row = front_place//2 + 1
        if pet_row - front_row < res_row - pet_row:
            res_place = front_place
            res_row = front_row

    if res_row > n//2 + 1 or res_place > n:
        return -1

    return f"{res_row} {2-res_place%2}"


f = open("input.txt")
lines = f.read().splitlines()
f.close()

print(solution(lines))