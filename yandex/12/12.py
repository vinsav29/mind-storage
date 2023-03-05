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


seq = input()
stack = Stack()
pairs = {")": "(", "]": "[", "}": "{"}
for s in seq:
    if s in "([{":
        stack.push(s)
    elif s in ")]}":
        if pairs[s] != stack.pop():
            print("no")
            break
else:
    if stack.length > 0:
        print("no")
    else:
        print("yes")
