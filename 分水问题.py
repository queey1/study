
from collections import deque

def solve():
    capacities = (8, 5, 3)
    start = (6, 0, 0)
    target = (4, 2, 0)
    visited = set()
    queue = deque()
    queue.append((start, []))

    while queue:
        state, path = queue.popleft()

        if state == target:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                current = list(state)
                pour = min(current[i], capacities[j] - current[j])
                current[i] -= pour
                current[j] += pour
                new_state = tuple(current)

                if new_state not in visited:
                    queue.append((new_state, path + [state]))

    return []  
# 运行并打印
steps = solve()
print("最优解步骤：")
for idx, s in enumerate(steps):
    print(f"步骤{idx}: {s}")