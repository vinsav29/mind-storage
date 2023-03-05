class Queue:
    def __init__(self):
        self.first = 0
        self.last = 0
        self.store = []

    def push(self, n):
        self.last += 1
        self.store.append(n)
        print("ok")

    def pop(self):
        if self.first == self.last:
            print("error")
            return
        print(self.store[self.first])
        self.first += 1
        # return self.store[self.first - 1]

    def front(self):
        if self.first == self.last:
            print("error")
            return
        print(self.store[self.first])

    def size(self):
        print(self.last - self.first)

    def clear(self):
        self.__init__()
        print("ok")

    # def exit(self):
    #     print("bye")

f = open("input.txt")
text = f.read()
f.close()

q = Queue()
cmd = ""
for cmd in text.splitlines():
# while cmd != "exit":
#     cmd = input()
    if cmd == "pop":
        q.pop()
    elif cmd == "front":
        q.front()
    elif cmd == "size":
        q.size()
    elif cmd == "clear":
        q.clear()
    elif cmd == "exit":
        break
    else:
        q.push(n=int(cmd.split()[-1]))
print("bye")