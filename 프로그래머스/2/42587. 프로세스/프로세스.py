from collections import deque

def solution(priorities, location):
    ans = 0
    q = deque(enumerate(priorities))
    while q:
        i, priority = q.popleft()
        if any(priority < p for _, p in q):
            q.append((i, priority))
        else:
            ans += 1
            if i == location:
                return ans