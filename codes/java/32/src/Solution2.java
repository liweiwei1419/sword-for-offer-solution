import java.util.ArrayList;
import java.util.LinkedList;


class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}

// 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
// 层序遍历
public class Solution {
    ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        if (pRoot == null) {
            return res;
        }
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.addLast(pRoot);

        while (!queue.isEmpty()) {
            int size = queue.size();

            ArrayList<Integer> curLevel = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode top = queue.removeFirst();
                curLevel.add(top.val);
                if (top.left != null) {
                    queue.addLast(top.left);
                }
                if (top.right != null) {
                    queue.addLast(top.right);
                }

            }
            res.add(curLevel);
        }
        return res;
    }
}