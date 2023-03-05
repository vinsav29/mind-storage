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


seq = input().split()
s = Stack()
for c in seq:
    if c == "+":
        s.push(s.pop() + s.pop())
    elif c == "-":
        dec = s.pop()
        res = s.pop() - dec
        s.push(res)
    elif c == "*":
        s.push(s.pop() * s.pop())
    else:
        s.push(int(c))
print(s.pop())