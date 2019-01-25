# LeetCode 中的路径问题

#### [257. 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths/)

要求：给定一个二叉树，返回所有从根节点到叶子节点的路径。

**说明:** 叶子节点是指没有子节点的节点。

**示例:**

```
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
```



说明：下面这是刘宇波老师的写法，感觉有点啰嗦。可以使用 dfs 完成。

Python 代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []

        if root is None:
            return []

        if root.left is None and root.right is None:
            res.append(str(root.val))
            return res

        left_paths = self.binaryTreePaths(root.left)
        for lpath in left_paths:
            res.append(str(root.val) + '->' + lpath)

        right_paths = self.binaryTreePaths(root.right)
        for rpath in right_paths:
            res.append(str(root.val) + '->' + rpath)

        return res
```

#### [112. 路径总和](https://leetcode-cn.com/problems/path-sum/)

要求：给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

**说明:** 叶子节点是指没有子节点的节点。

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        assert root != null;
        // 如果没有左子树和右子树，就说明是根结点了
        if (root.left == null && root.right == null) {
            return root.val == sum;
        }

        boolean hasPathSum = false;
        if (root.left != null) {
            hasPathSum = hasPathSum || hasPathSum(root.left, sum - root.val);
        }
        if (root.right != null) {
            hasPathSum = hasPathSum || hasPathSum(root.right, sum - root.val);
        }
        return hasPathSum;
    }
}
```

#### [437. 路径总和 III](https://leetcode-cn.com/problems/path-sum-iii/)

要求：给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

**示例：**

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
```

动态规划：

Python 代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        from collections import defaultdict
        memo = defaultdict(int)
        # 记忆化递归，memo 表示缓存
        memo[0] = 1  # 表示 cur - sum = 0, return 1
        self.res = 0

        def helper(root, curSum):
            if root is None:
                return
            curSum += root.val
            self.res += memo[curSum - sum]
            memo[curSum] += 1

            helper(root.left, curSum)
            helper(root.right, curSum)
            memo[curSum] -= 1

        helper(root, 0)
        return self.res
```

