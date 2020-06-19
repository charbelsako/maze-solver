from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue
from node import Node


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: object = field()


# q = PriorityQueue()
# # you can change the representation of your objects to include the f value only
# # https://docs.python.org/3/library/dataclasses.html
# n = Node('a', 0, 0)
# n.f = 1
# n2 = Node('b', 0, 0)
# n2.f = 0
# n3 = Node('c', 0, 0)
# n3.f = 2
# q.put(PrioritizedItem(n.f, n))
# q.put(PrioritizedItem(n2.f, n2))
# q.put(PrioritizedItem(n3.f, n3))
# print(q.get())
