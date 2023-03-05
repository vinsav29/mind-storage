class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Dequeue:
    def __init__(self):
        self.first: Node | None = None
        self.last: Node | None = None
        self.len = 0

    def push_front(self, n):
        new_node = Node(n, next=self.first)

        if self.len == 0:
            # set new node as last pointer
            self.last = new_node
        else:
            self.first.prev = new_node
        self.first = new_node
        self.len += 1
        return "ok"

    def push_back(self, n):
        new_node = Node(n, prev=self.last)

        if self.len == 0:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.len += 1
        return "ok"

    def pop_front(self):
        if self.len == 0:
            return "error"
        res = self.first.val
        self.first = self.first.next
        if self.len == 1:
            self.last = None
        else:
            self.first.prev = None
        self.len -= 1
        return res

    def pop_back(self):
        if self.len == 0:
            return "error"
        res = self.last.val
        self.last = self.last.prev
        if self.len == 1:
            self.first = None
        else:
            self.last.next = None
        self.len -= 1
        return res

    def front(self):
        if self.len == 0:
            return "error"
        return self.first.val

    def back(self):
        if self.len == 0:
            return "error"
        return self.last.val

    def size(self):
        return self.len

    def clear(self):
        self.__init__()
        return "ok"

f = open("input.txt")
text = f.read()
f.close()

dq = Dequeue()
cmd = ""
for cmd in text.splitlines():
    if cmd == "exit":
        print("bye")
        break
    if len(cmd) > 10:
        cmd, n = cmd.split()
        method = getattr(dq, cmd)
        print(method(int(n)))
        continue
    method = getattr(dq, cmd)
    print(method())
