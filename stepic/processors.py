from heapq import heappop, heappush


def main():
    n_proc, m_tasks = map(int, input().split())
    tasks_durations = list(map(int, input().split()))
    heap = [(0, proc_id) for proc_id in range(n_proc)]
    for task in range(m_tasks):
        finish_time, proc_id = heappop(heap)
        heappush(heap, (finish_time+tasks_durations[task], proc_id))
        print(proc_id, finish_time)


if __name__ == '__main__':
    main()
