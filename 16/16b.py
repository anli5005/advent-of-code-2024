import sys
import re
from collections import *
from itertools import *
from heapq import *
from dataclasses import *
import math

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
lines = inp.split("\n")
m = len(lines)
n = len(lines[0])

grid = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
# dirs = dirs + diag

start_pos = None
end_pos = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == "S":
            start_pos = (i, j)
        elif grid[i][j] == "E":
            end_pos = (i, j)

State = namedtuple("State", ["cost", "node", "parent"])
Node = namedtuple("Node", ["pos", "dir"])

@dataclass
class NodeData:
    cost: int
    parents: list[Node]

print("Running Djikstra's...")

q = [State(0, Node(start_pos, 0), None)]
visited = {}
while q:
    current = heappop(q)

    if grid[current.node.pos[0]][current.node.pos[1]] == "#":
        continue
    
    if current.node in visited:
        if current.cost == visited[current.node].cost:
            visited[current.node].parents.append(current.parent)
        elif current.node.pos == end_pos:
            break
        continue
    
    visited[current.node] = NodeData(current.cost, [])
    if current.parent is not None:
        visited[current.node].parents.append(current.parent)

    d = dirs[current.node.dir]
    heappush(q, State(current.cost + 1, Node((current.node.pos[0] + d[0], current.node.pos[1] + d[1]), current.node.dir), current.node))
    for delta in [-1, 1]:
        new_index = (current.node.dir + delta + len(dirs)) % len(dirs)
        heappush(q, State(current.cost + 1000, Node(current.node.pos, new_index), current.node))

print("Backtracking...")

seen_nodes = set()
seen_positions = set()

q = deque()
for key in visited.keys():
    if key.pos == end_pos:
        q.append(key)

while q:
    current = q.popleft()
    if current in seen_nodes:
        continue

    seen_nodes.add(current)
    seen_positions.add(current.pos)

    for parent in visited[current].parents:
        q.append(parent)

for i in range(m):
    row = ""
    for j in range(n):
        if (i, j) in seen_positions:
            row += "O"
        else:
            row += grid[i][j]
    print(row)

print(len(seen_positions))