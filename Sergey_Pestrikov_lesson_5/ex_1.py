# Реализовать обход дерева post-order. Сначала левое, потом правое поддерево, в последнюю очередь корень

class Solution:
    def postorderTraversal(selfself, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            answer.append(node.val)

        if not root:
            return answer
        helper(root)

        return answer