class Heap:
    def __init__(self):
        self.store = []

    def insert(self, k):
        self.store.append(k)
        ptr = len(self.store) - 1
        while ptr > 0 and self.store[ptr] > self.store[(ptr-1)//2]:
            self.store[ptr], self.store[(ptr-1)//2] = self.store[(ptr-1)//2], self.store[ptr]
            ptr = (ptr-1)//2
        return

    def extract(self):
        res = self.store[0]
        self.store[0] = self.store[-1]
        pos = 0
        while pos*2+2 < len(self.store):
            min_son_index = pos*2 + 1
            if self.store[pos*2 + 2] > self.store[min_son_index]:
                min_son_index = pos*2 + 2
            if self.store[pos] < self.store[min_son_index]:
                self.store[pos], self.store[min_son_index] = self.store[min_son_index], self.store[pos]
                pos = min_son_index
            else:
                break
        self.store.pop()
        return res

f = open("input.txt")
lines = f.read().splitlines()
f.close()

total = int(lines[0])
heap = Heap()
for i in range(1, total + 1):

    cmd = lines[i].split()
    if len(cmd) > 1:
        heap.insert(int(cmd[1]))
    else:
        print(heap.extract())
