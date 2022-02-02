import sys
input = sys.stdin.readline
import heapq


T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    heap_max, heap_min = [], []
    visited = [False for _ in range(1000000)]
    for id in range(k):
        command, num = input().strip().split()
        num = int(num)
        if command == 'I':
            # num이 tuple의 첫 번째 값으로 들어가야 한다.
            # 왜냐하면 그래야 값이 최소부터로 정렬이 되기 때문이다.
            heapq.heappush(heap_max, (-num, id))
            heapq.heappush(heap_min, (num, id))
            # 방문 처리
            visited[id] = True
        elif command == 'D':
            if num == 1:
                # 만약 max값에서 이 숫자를 빼는게 처음일 때에는 들어가지 않는다.
                # 근데 min값에서 이미 뺀 숫자면(visited가 False이면) 그냥 뺀다.
                while heap_max and not visited[heap_max[0][1]]:
                    heapq.heappop(heap_max)
                # 이제 max값을 뺄 것이다.
                if heap_max:
                    visited[heap_max[0][1]] = False
                    heapq.heappop(heap_max)
            elif num == -1:
                while heap_min and not visited[heap_min[0][1]]:
                    heapq.heappop(heap_min)
                if heap_min:
                    visited[heap_min[0][1]] = False
                    heapq.heappop(heap_min)
    # 남은 동기화를 해야 한다. (양쪽에서 뺀 값들 빼기)
    while heap_max and not visited[heap_max[0][1]]:
        heapq.heappop(heap_max)
    while heap_min and not visited[heap_min[0][1]]:
        heapq.heappop(heap_min)

    if not heap_max or not heap_min:
        print("EMPTY")
    else:
        print(-heapq.heappop(heap_max)[0], heapq.heappop(heap_min)[0])