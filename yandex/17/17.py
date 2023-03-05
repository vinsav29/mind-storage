class Queue:
    def __init__(self, nums):
        self.first = 0
        self.last = 5
        self.store = list(map(int, nums.split()))

    def push(self, n):
        self.last += 1
        self.store.append(n)
        return

    def pop(self):
        if self.first == self.last:
            print("error")
            return None
        first_el = self.store[self.first]
        self.first += 1
        return first_el

    def front(self):
        if self.first == self.last:
            print("error")
            return
        return self.store[self.first]

    def size(self):
        return self.last - self.first

    # def clear(self):
    #     self.__init__()
    #     print("ok")

    # def exit(self):
    #     print("bye")

f = open("input.txt")
nums = f.read().splitlines()
f.close()


q1 = Queue(nums[0])
q2 = Queue(nums[1])
step = 0
while True:
    card1, card2 = q1.front(), q2.front()
    diff = card1 - card2
    if diff == -9:
        q = q1
    elif diff == 9:
        q = q2
    elif diff > 0:
        q = q1
    else:
        q = q2
    q.push(card1)
    q.push(card2)
    q1.pop()
    q2.pop()
    step += 1

    if q1.size() == 0:
        print(f"second {step}")
        break
    if q2.size() == 0:
        print(f"first {step}")
        break
    if step == 10**6:
        print("botva")
        break