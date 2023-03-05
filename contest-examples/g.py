from collections import defaultdict


def solution(n, friends):

    for my in range(1, n + 1):
        recomm = dict()
        max_count = 0
        for friend_id in friends[my]:   # my_id -> set(id_1 .. id_n)

            # get friends of my friend and save to recommendations
            friends_of_my_friend = friends[friend_id]
            for fof_id in friends_of_my_friend:
                if fof_id == my or fof_id in friends[my]:
                    continue

                # save like {me: {friend_id: count}}
                count = recomm.get(fof_id, 0) + 1
                recomm[fof_id] = count
                if count > max_count:
                    max_count = count

        fin = [k for k, v in recomm.items() if v == max_count]

        if len(fin) == 0:
            print(0)
        elif len(fin) == 1:
            print(*fin)
        else:
            print(" ".join(map(str, sorted(fin))))


n, m = map(int, input().split())
friends = defaultdict(set)
for _ in range(m):
    biba, boba = map(int, input().split())
    friends[biba].add(boba)
    friends[boba].add(biba)
# print(friends)
solution(n, friends)

