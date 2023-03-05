import heapq

n, m = map(int, input().split())
energy = list(map(int, input().split()))
heapq.heapify(energy)

scheduler = []
consumption = 0
for _ in range(m):
    t, task = map(int, input().split())
    while len(scheduler) > 0 and scheduler[0][0] <= t:
        free_cpu = heapq.heappop(scheduler)
        heapq.heappush(energy, free_cpu[1])
    if len(energy) > 0:
        cpu = heapq.heappop(energy)
        heapq.heappush(scheduler, (t + task, cpu))
        consumption += cpu * task
    else:
        # pass task
        continue
print(consumption)