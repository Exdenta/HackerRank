import time
import random
from collections import deque


class Node:
    def __init__(self, value='N', left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dfs_serialize(root: Node) -> list:
    """ Dfs serialization algorithm
    """
    node_list = list()
    Q = deque()
    Q.appendleft(root)

    while Q:
        node = Q.popleft()
        if node != None:
            node_list.append(node.value)
            Q.appendleft(node.right)
            Q.appendleft(node.left)
        else:
            node_list.append(None)

    return node_list


def recursion_dfs_serialize(root: Node) -> list:
    """ Bad dfs serialization algorithm
    """
    if root == None:
        return [None]
    left_serialize = recursion_dfs_serialize(root.left)
    right_serialize = recursion_dfs_serialize(root.right)
    return [root.value] + left_serialize + right_serialize


def dfs_serialize(root: Node) -> list:
    """ Dfs serialization algorithm
    """
    node_list = list()
    Q = deque()
    Q.appendleft(root)

    while Q:
        node = Q.popleft()
        if node != None:
            node_list.append(node.value)
            Q.appendleft(node.right)
            Q.appendleft(node.left)
        else:
            node_list.append(None)

    return node_list


def bfs_deserialize(node_list: list) -> Node:
    """ Bfs deserialization algorithm
    """
    assert len(node_list) != 0
    root = None
    if len(node_list) > 0:
        root = Node(node_list[0], 'N', 'N')
        not_visited_nodes = deque()
        not_visited_nodes.appendleft(root)

        for idx in range(1, len(node_list)):
            if node_list[idx] != None:
                node = not_visited_nodes[0]
                if node.left == 'N':
                    node.left = Node(node_list[idx], 'N', 'N')
                    not_visited_nodes.append(node.left)
                elif node.right == 'N':
                    node.right = Node(node_list[idx], 'N', 'N')
                    not_visited_nodes.append(node.right)
                    not_visited_nodes.popleft()

    return root


def dfs_deserialize(node_list: list) -> Node:
    """ Dfs deserialization algorithm
    """
    assert len(node_list) != 0
    root = None
    if len(node_list) > 0:
        root = Node(node_list[0], 'N', 'N')
        not_visited_nodes = deque()
        not_visited_nodes.appendleft(root)

        for idx in range(1, len(node_list)):
            node = not_visited_nodes[0]
            if node_list[idx] != None:
                if node.left == 'N':
                    node.left = Node(node_list[idx], 'N', 'N')
                    not_visited_nodes.appendleft(node.left)
                elif node.right == 'N':
                    node.right = Node(node_list[idx], 'N', 'N')
                    not_visited_nodes.append(node.right)
                    not_visited_nodes.popleft()
            else:
                if node.left == 'N':
                    node.left = None
                elif node.right == 'N':
                    node.right = None
                    not_visited_nodes.popleft()
    return root


def generate_binary_tree(node_count: int) -> Node:
    root = Node(random.randint(0, 100), None, None)
    avail_nodes = deque()
    avail_nodes.append(root)

    for i in range(0, node_count):
        N = Node(random.randint(0, 100), None, None)
        avail_node = avail_nodes[0]

        if avail_node.left == None:
            avail_node.left = N
            avail_nodes.append(N)
        elif avail_node.right == None:
            avail_node.right = N
            avail_nodes.append(N)
            avail_nodes.popleft()
        else:
            avail_nodes.popleft()
    return root


def main():
    # """
    #         7
    #     /      \
    #     6       3
    #    / \     / \
    #    5  N    2  1
    # """
    # node1 = Node(1, None, None)
    # node2 = Node(2, None, None)
    # node3 = Node(3, node2, node1)
    # # node4 = Node(4, None, None)
    # node5 = Node(5, None, None)
    # node6 = Node(6, node5, None)
    # root = Node(7, node6, node3)

    root = generate_binary_tree(10000000)

    # serialize 1
    tic = time.perf_counter()
    node_list = recursion_dfs_serialize(root)
    toc = time.perf_counter()
    # print(node_list)
    print(f"Recursion serialization alg: {toc - tic:0.4f} seconds")

    # serialize 2
    tic = time.perf_counter()
    node_list = dfs_serialize(root)
    toc = time.perf_counter()
    # print(node_list)
    print(f"Serialization alg: {toc - tic:0.4f} seconds")

    # deserialize
    root = dfs_deserialize(node_list)
    print(root.value)


if __name__ == "__main__":
    main()
