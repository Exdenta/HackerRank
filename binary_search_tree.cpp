#include <stdexcept>
#include <string>
#include <iostream>
#include <stack>
#include <ctime>

// Binary search tree (BST) is a binary tree where the value of each node is larger or equal to the values 
// in all the nodes in that node's left subtree and is smaller than the values in all the nodes in that node's right subtree.
// Write a function that, efficiently with respect to time used, checks if a given binary search tree contains a given value.

// For example, for the following tree:

// n1 (Value: 1, Left: null, Right: null)
// n2 (Value: 2, Left: n1, Right: n3)
// n3 (Value: 3, Left: null, Right: null)
// Call to contains(n2, 3) should return true since a tree with root at n2 contains number 3.


class Node
{
public:
    Node() {}

    Node(int value, Node *left, Node *right)
    {
        this->value = value;
        this->left = left;
        this->right = right;
    }

    int getValue() const
    {
        return value;
    }

    Node *getLeft() const
    {
        return left;
    }

    Node *getRight() const
    {
        return right;
    }

private:
    int value;
    Node *left;
    Node *right;
};

class BinarySearchTree
{
public:

    static bool contains(const Node &root, int value)
    {
        std::stack<Node> unexplored_nodes;
        unexplored_nodes.push(root);

        Node v;
        while (!unexplored_nodes.empty())
        {
            v = unexplored_nodes.top();
            unexplored_nodes.pop();

            if (v.getValue() == value)
                return true;
            else if (v.getValue() > value && v.getLeft())
                unexplored_nodes.push(*(v.getLeft()));
            else if (v.getRight())
                unexplored_nodes.push(*(v.getRight()));
        }

        return false;

    }

    // recursive method
    static bool contains_recursive(const Node &root, int value)
    {
        if (root.getValue() == value)
        {
            return true;
        }
        else if (root.getValue() < value)
        {
            if (root.getRight())
                return contains(*(root.getRight()), value);
        }
        else
        {
            if (root.getLeft())
                return contains(*(root.getLeft()), value);
        }
        return false;
    }
};

#ifndef RunTests
int main()
{
    Node n1(1, NULL, NULL);
    Node n3(3, NULL, NULL);
    Node n2(2, &n1, &n3);

    clock_t Begin, End;
    Begin = clock() * 1000;

    std::cout << std::boolalpha << BinarySearchTree::contains(n2, 3) << std::endl;

    End = clock() * 1000;
    auto elapTicks = End - Begin;
    auto elapMilli = elapTicks / 1000;
    std::cout << elapMilli << "ms." << std::endl;
}
#endif