class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_tree_string(s):
    s = s.replace(' ', '')
    return build_tree_from_string(s)

def build_tree_from_string(s):
    stack = []
    i = 0
    n = len(s)

    while i < n:
        if s[i].isdigit():
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            node = TreeNode(num)
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
        elif s[i] == ')':
            stack.pop()
        i += 1

    return stack[0] if stack else None

def pre_order_traversal(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# Пример использования
input_string = "8 (3 (1, 6 (4, 7)), 10 (, 14 (13,)))"

print(pre_order_traversal(parse_tree_string(input_string)))
