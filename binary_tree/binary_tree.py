#!/usr/bin/env python
#filename: binaryTree.py
#

from collections import namedtuple
from sys import stdout

''''
         a
        / \
       /   \
      /     \
     b       c
    /       / \
   d       e   f
    \           \
     g           h
'''

Node = namedtuple('Nodes', ['data','left','right'])
tree = Node('a',
            Node('b',
                 Node('d',
                      None,
                      Node('g', None, None)),
                 None),
            Node('c',
                 Node('e', None, None),
                 Node('f',
                      None,
                      Node('h', None, None)),
                 ))

def visitor(i):
    stdout.write("%s "%i)

def traversal(node, order):
    if not node: return
    op = {
            'N': lambda:visitor(node.data),
            'L': lambda:traversal(node.left, order),
            'R': lambda:traversal(node.right, order),
    }
    for x in order:
        op[x]()

for order in ['NLR', 'LNR', 'LRN']:
    traversal(tree, order)
    print
