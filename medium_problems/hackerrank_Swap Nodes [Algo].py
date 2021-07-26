#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

sys.setrecursionlimit(10000) # recursion limit



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def swapNodes(indexes, queries):
    def create(root, indexes):
        q = deque()
        q.append(root)
        for l, r in indexes:
            temp = q.popleft()
            if l != -1:
                temp.left = Node(l)
                q.append(temp.left)
            if r != -1:
                temp.right = Node(r)
                q.append(temp.right)
        return root

    def swap(root, k, level):
        if root is None:
            return
        if level % k == 0:
            root.left, root.right = root.right, root.left
        swap(root.left, k, level + 1)
        swap(root.right, k, level + 1)

    def inOrder(root, result):
        if root is None:
            return
        inOrder(root.left, result)
        result.append(root.val)
        inOrder(root.right, result)

    root = Node(1)
    root = create(root, indexes)
    result = []
    for k in queries:
        l = []
        swap(root, k, 1)  # 1 == current level
        inOrder(root, l)
        result.append(l)
    print(result)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
