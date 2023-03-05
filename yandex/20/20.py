class Heap:
    def __init__(self, arr):
        self.store = arr

    def insert(self, k):
        self.store.append(k)
        ptr = len(self.store) - 1
        while ptr > 0 and self.store[ptr] > self.store[(ptr-1)//2]:
            self.store[ptr], self.store[(ptr-1)//2] = self.store[(ptr-1)//2], self.store[ptr]
            ptr = (ptr-1)//2
        return

    def extract(self, length):
        res = self.store[0]
        self.store[0] = self.store[length-1]
        pos = 0
        while pos*2+2 < length:
            min_son_index = pos*2 + 1
            if self.store[pos*2 + 2] > self.store[min_son_index]:
                min_son_index = pos*2 + 2
            if self.store[pos] < self.store[min_son_index]:
                self.store[pos], self.store[min_son_index] = self.store[min_son_index], self.store[pos]
                pos = min_son_index
            else:
                break
        # self.store.pop()
        self.store[length - 1] = res
        return res

    def heapify(self):
        last = len(self.store) - 1
        for i in range(last, -1, -1):
            pos = i
            while pos * 2 + 1 <= last:

                min_son_index = pos * 2 + 1

                # check second son exists
                if min_son_index + 1 <= last and self.store[min_son_index] < self.store[min_son_index+1]:
                    min_son_index += 1

                # swap pos and min son
                if self.store[pos] < self.store[min_son_index]:
                    self.store[pos], self.store[min_son_index] = self.store[min_son_index], self.store[pos]
                else:
                    break

                # set pos = min son
                pos = min_son_index

f = open("input.txt")
lines = f.read().splitlines()
f.close()

total = int(lines[0])
arr = list(map(int, lines[1].split()))
heap = Heap(arr)
heap.heapify()
length = len(arr)
while length > 1:
    heap.extract(length)
    length -= 1
print(" ".join(map(str, heap.store)))