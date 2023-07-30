# https://www.acmicpc.net/problem/1991
# 전위 순회 : 루트 -> 왼쪽자식 -> 오른쪽 자식
# 중위 순회 : 왼쪽자식 -> 루트 -> 오른쪽 자식
# 후위 순회 : 왼쪽자식 -> 오른쪽자식 -> 루트

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(node.left_node)
    if node.right_node != '.':
        pre_order(node.right_node)
def in_order(node):
    if node.left_node != '.':
        in_order(node.left_node)
    print(node.data, end='')
    if node.right_node != '.':
        in_order(node.right_node)

def post_order(node):
    if node.left_node != '.':
        in_order(node.left_node)
    if node.right_node != '.':
        in_order(node.right_node)
    print(node.data, end='')

n = int(input())
tree = {}
for i in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node=left_node, right_node=right_node)
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])