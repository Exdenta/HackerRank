#include <iostream>
#include <any>
#include <string>
#include <stack>
#include <deque>

class Node
{
public:
    int32_t value;
    Node* left;
    Node* right;

    Node(int32_t value, Node* left, Node* right)
        : value{ value }
        , left{ left }
        , right{ right }
    {}

    ~Node()
    {
        if (left) delete left;
        if (right) delete right;
    }
};

//
// bfs tree serialization
//
std::deque<int32_t*> bfs_serialization(Node* root)
{
    std::deque<int32_t*> node_list;
    std::deque<Node*> not_visited_nodes;
    not_visited_nodes.push_back(root);

    while (!not_visited_nodes.empty())
    {
        auto node = not_visited_nodes[0];
        if (node != nullptr)
        {
            node_list.push_back(new int32_t(node->value));
            not_visited_nodes.push_back(node->left);
            not_visited_nodes.push_back(node->right);
        }
        else
        {
            node_list.push_back(nullptr);
        }
        not_visited_nodes.pop_front();
    }

    return node_list;
}

//
// TODO: bfs tree deserialization
//
Node* bfs_deserialization(std::deque<int32_t*>& list)
{
    if (list.size() == 0)
        return nullptr;

    Node* root = new Node{ *list[0], nullptr, nullptr };
    std::deque<Node*> bottom_nodes;
    bottom_nodes.push_back(root);

    for (int32_t* node_value : list)
    {
        if (node_value)
        {
            Node* node = new Node{ *node_value, nullptr, nullptr };
            Node* bottom_node = bottom_nodes[0];
            if (bottom_node->left == nullptr)
            {
                bottom_node->left = node;
                bottom_nodes.push_back(node);
            }
            else if (bottom_node->right == nullptr)
            {
                bottom_node->right = node;
                bottom_nodes.push_back(node);
                bottom_nodes.pop_front();
            }
        }
    }

    return root;
}

//
// Print tree node values
//
void print_tree(std::deque<int32_t*>& list)
{
    for (auto node : list)
        if (node != nullptr)
            std::cout << *node << " ";
        else std::cout << " None ";
}


int main()
{
    // # """
    // #         7
    // #     /      \
    // #     6       3
    // #    / \     / \
    // #    5  N    2  1
    // # """

    auto node1 = new Node{ 1, nullptr, nullptr };
    auto node2 = new Node{ 2, nullptr, nullptr };
    auto node3 = new Node{ 3, node2, node1 };
    // auto node2 = new Node{ 4, nullptr, nullptr };
    auto node5 = new Node{ 5, nullptr, nullptr };
    auto node6 = new Node{ 6, node5, nullptr };
    auto root = new Node{ 7, node6, node3 };

    std::deque<int32_t*> serialized_tree = bfs_serialization(root);
    print_tree(serialized_tree);
    Node* node = bfs_deserialization(serialized_tree);

    // //
    // //
    // //
    // std::cout << std::endl;
    // auto new_tree = bfs_serialization(node);
    // print_tree(new_tree);


    delete root;
    delete node;
    return 0;
}







// import random
// from collections import deque
// import time
// from memory_profiler import profile


// class Node :
//     def __init__(self, value = 'N', left = None, right = None) :
//     self.value = value
//     self.left = left
//     self.right = right


//     def dfs_serialize(root: Node)->list:
// """ Dfs serialization algorithm
// """
// node_list = list()
// Q = deque()
// Q.appendleft(root)

// while Q:
// node = Q.popleft()
// if node != None :
//     node_list.append(node.value)
//     Q.appendleft(node.right)
//     Q.appendleft(node.left)
// else:
// node_list.append(None)

// return node_list


// def recursion_dfs_serialize(root: Node)->list:
// """ Bad dfs serialization algorithm
// """
// if root == None :
//     return[None]
//     left_serialize = recursion_dfs_serialize(root.left)
//     right_serialize = recursion_dfs_serialize(root.right)
//     return[root.value] + left_serialize + right_serialize


//     def dfs_serialize(root: Node)->list:
// """ Dfs serialization algorithm
// """
// node_list = list()
// Q = deque()
// Q.appendleft(root)

// while Q:
// node = Q.popleft()
// if node != None :
//     node_list.append(node.value)
//     Q.appendleft(node.right)
//     Q.appendleft(node.left)
// else:
// node_list.append(None)

// return node_list


// def bfs_deserialize(node_list: list)->Node:
// """ Bfs deserialization algorithm
// """
// assert len(node_list) != 0
// root = None
// if len(node_list) > 0:
// root = Node(node_list[0], 'N', 'N')
// not_visited_nodes = deque()
// not_visited_nodes.appendleft(root)

// for idx in range(1, len(node_list)) :
//     if node_list[idx] != None :
//         node = not_visited_nodes[0]
//         if node.left == 'N' :
//             node.left = Node(node_list[idx], 'N', 'N')
//             not_visited_nodes.append(node.left)
//             elif node.right == 'N' :
//             node.right = Node(node_list[idx], 'N', 'N')
//             not_visited_nodes.append(node.right)
//             not_visited_nodes.popleft()

//             return root


//             def dfs_deserialize(node_list: list)->Node:
// """ Dfs deserialization algorithm
// """
// assert len(node_list) != 0
// root = None
// if len(node_list) > 0:
// root = Node(node_list[0], 'N', 'N')
// not_visited_nodes = deque()
// not_visited_nodes.appendleft(root)

// for idx in range(1, len(node_list)) :
//     node = not_visited_nodes[0]
//     if node_list[idx] != None :
//         if node.left == 'N' :
//             node.left = Node(node_list[idx], 'N', 'N')
//             not_visited_nodes.appendleft(node.left)
//             elif node.right == 'N' :
//             node.right = Node(node_list[idx], 'N', 'N')
//             not_visited_nodes.append(node.right)
//             not_visited_nodes.popleft()
//         else:
// if node.left == 'N' :
//     node.left = None
//     elif node.right == 'N' :
//     node.right = None
//     not_visited_nodes.popleft()
//     return root


//     def generate_binary_tree(node_count: int)->Node:
// root = Node(random.randint(0, 100), None, None)
// avail_nodes = deque()
// avail_nodes.append(root)

// for i in range(0, node_count) :
//     N = Node(random.randint(0, 100), None, None)
//     avail_node = avail_nodes[0]

//     if avail_node.left == None :
//         avail_node.left = N
//         avail_nodes.append(N)
//         elif avail_node.right == None :
//         avail_node.right = N
//         avail_nodes.append(N)
//         avail_nodes.popleft()
//     else:
// avail_nodes.popleft()
// return root


// def main() :
// # """
//     #         7
// #     /      \
//     #     6       3
// #    / \     / \
//     #    5  N    2  1
// # """
//     # node1 = Node(1, None, None)
//     # node2 = Node(2, None, None)
//     # node3 = Node(3, node2, node1)
// # # node4 = Node(4, None, None)
//     # node5 = Node(5, None, None)
//     # node6 = Node(6, node5, None)
//     # root = Node(7, node6, node3)

//     root = generate_binary_tree(10000000)

//     # serialize 1
//     tic = time.perf_counter()
//     node_list = recursion_dfs_serialize(root)
//     toc = time.perf_counter()
//     # print(node_list)
//     print(f"Recursion serialization alg: {toc - tic:0.4f} seconds")

//     # serialize 2
//     tic = time.perf_counter()
//     node_list = dfs_serialize(root)
//     toc = time.perf_counter()
//     # print(node_list)
//     print(f"Serialization alg: {toc - tic:0.4f} seconds")

//     # deserialize
//     root = dfs_deserialize(node_list)
//     print(root.value)


//     if __name__ == "__main__":
// main()
