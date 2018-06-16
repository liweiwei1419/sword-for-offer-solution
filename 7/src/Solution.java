class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Solution {

    public TreeNode reConstructBinaryTree(int[] pre, int[] in) {
        TreeNode root = reConstructBinaryTree(pre, 0, pre.length - 1, in, 0, in.length - 1);
        return root;
    }

    /**
     * 根据前序遍历数组的 [preL, preR] 和 中序遍历数组的 [inL, inR] 重新组建二叉树
     *
     * @param pre  前序遍历数组
     * @param preL 前序遍历数组的区间左端点
     * @param preR 前序遍历数组的区间右端点
     * @param in   中序遍历数组
     * @param inL  中序遍历数组的区间左端点
     * @param inR  中序遍历数组的区间右端点
     * @return 构建的新二叉树的根结点
     */
    private TreeNode reConstructBinaryTree(int[] pre, int preL, int preR, int[] in, int inL, int inR) {
        if (preL > preR || inL > inR) {
            return null;
        }
        // 构建的新二叉树的根结点一定是前序遍历数组的第 1 个元素
        TreeNode root = new TreeNode(pre[preL]);
        // 从中序遍历的左区间端点开始找，找到和前序遍历数组的第 1 个元素的值相等的节点
        int i = inL;
        while (in[i] != pre[preL] && i <= inR) {
            i++;
        }
        // 在中序遍历数组中遍历了几个元素： i - inL
        // 接下来就是递归调用，关键的地方在于找前序遍历数组和中序遍历数组对应的区间的端点
        root.left = reConstructBinaryTree(pre, preL + 1, preL + (i - inL), in, inL, i - 1);
        root.right = reConstructBinaryTree(pre, preL + (i - inL) + 1, preR, in, i + 1, inR);
        return root;
    }
}