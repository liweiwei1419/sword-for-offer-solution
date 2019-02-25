class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;
    }
}

public class Solution {

    private TreeNode linkedListTail;
    private TreeNode res;

    public TreeNode Convert(TreeNode pRootOfTree) {
        convert(pRootOfTree);
        return res;
    }

    /**
     * 中序遍历
     *
     * @param root
     */
    private void convert(TreeNode root) {
        if (root == null) {
            return;
        }
        convert(root.left);
        // 中序遍历真正做事情的地方
        if (linkedListTail == null) { // 对应刚开始的时候
            linkedListTail = root;
            // 在最左边的地方记录需要返回的双向链表的根结点
            res = root;
        } else {
            linkedListTail.right = root;
            root.left = linkedListTail;
            linkedListTail = root;
        }
        convert(root.right);
    }
}