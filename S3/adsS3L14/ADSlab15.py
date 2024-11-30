class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_tree_string(s):
    s = s.replace(' ', '')
    return _parse_tree(s, [0])

def _parse_tree(s, index):
    if index[0] >= len(s) or s[index[0]] == ')':
        return None

    value = ''
    while index[0] < len(s) and s[index[0]].isdigit():
        value += s[index[0]]
        index[0] += 1

    if value == '':
        return None

    node = TreeNode(int(value))

    # Если следующий символ - '(', это значит, что у нас есть поддеревья
    if index[0] < len(s) and s[index[0]] == '(':
        index[0] += 1  # Пропускаем '('
        node.left = _parse_tree(s, index)
        index[0] += 1
        node.right = _parse_tree(s, index)
        index[0] += 1

    return node

def preorder_traversal(node):
    if node is None:
        return ''
    return str(node.value) + ' ' + preorder_traversal(node.left) + preorder_traversal(node.right)

def inorder_traversal(node):
    if node is None:
        return ''
    return inorder_traversal(node.left) + str(node.value) + ' ' + inorder_traversal(node.right)

def postorder_traversal(node):
    if node is None:
        return ''
    return postorder_traversal(node.left) + postorder_traversal(node.right) + str(node.value) + ' '

# Пример использования
input_string = "8 (3 (1, 6 (4, 7)), 10 (, 14 (13,)))"
root = parse_tree_string(input_string)

print("Прямой обход:", preorder_traversal(root).strip())
print("Центральный обход:", inorder_traversal(root).strip())
print("Концевой обход:", postorder_traversal(root).strip())
