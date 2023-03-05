
class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, n):
        self.stack.append(n)
        self.length += 1
        return "ok"

    def pop(self):
        if self.length == 0:
            return "error"
        self.length -= 1
        return self.stack.pop(-1)

    def back(self):
        if self.length == 0:
            return "error"
        return self.stack[-1]

    def size(self):
        return self.length

    def clear(self):
        self.stack.clear()
        self.length = 0
        return "ok"

    def exit(self):
        return "bye"


# def solution(commands):
#     s = Stack()
#     for cmd in commands:
#         if len(cmd) >= 6:
#             print(s.push(int(cmd.split()[-1])))
#         else:
#             foo = getattr(s, cmd)
#             ans = foo()
#             print(ans)
#             if ans == " bye":
#                 return
#
#
# with open("input.txt") as f:
#     text = f.read()
#     solution(text.splitlines())

def sol():
    s = Stack()
    while True:
        cmd = input()
        if len(cmd) >= 6:
            print(s.push(int(cmd.split()[-1])))
        else:
            foo = getattr(s, cmd)
            ans = foo()
            print(ans)
            if ans == "bye":
                return

sol()