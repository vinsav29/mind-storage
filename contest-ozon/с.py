def solution(s):
    res = ""
    while len(s) > 0:
        try:
            int(s[0])
        except ValueError:
            pass
        else:
            return ("-")

        try:
            int(s[1])
        except (ValueError, IndexError):
            return ("-")

        try:
            int(s[2])
        except IndexError:
            return ("-")
        except ValueError:
            # A1AA
            try:
                int(s[3])
            except ValueError:
                # valid A1AA
                res += s[:4] + " "
                s = s[4:]
            except IndexError:
                return ("-")
            else:
                return ("-")
        else:
            # A11AA
            try:
                int(s[3])
            except ValueError:
                # valid A11AA
                pass
            except IndexError:
                return ("-")
            else:
                return ("-")

            try:
                int(s[4])
            except ValueError:
                # valid A11AA
                res += s[:5] + " "
                s = s[5:]
            except IndexError:
                return ("-")
            else:
                return ("-")



        # if not isinstance(s[0], str) or not isinstance(s[1], int):
        #     return("-")
        # if isinstance(s[2], int) and isinstance(s[3], str) and isinstance(s[4], str):
        #     res += s[:5] + " "
        #     s = s[5:]
        # elif isinstance(s[2], str) and isinstance(s[3], str):
        #     res += s[:4] + " "
        #     s = s[4:]
        # else:
        #     return ("-")
    return res


t = int(input())

for i in range(t):
    # s = list(input())
    s = input()
    # a = list(map(int, input().split()))
    print(solution(s))
