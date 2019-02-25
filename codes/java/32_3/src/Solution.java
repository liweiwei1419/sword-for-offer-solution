import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Stack;

class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}

//  1
// 3 2
// 4 5 6
//12 11 10 9 8 7
// 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
// 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
public class Solution {
    public ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        if (pRoot == null) {
            return res;
        }
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.addLast(pRoot);
        boolean right = true;
        while (!queue.isEmpty()) {
            int size = queue.size();
            // 之 字形 一开始向右
            ArrayList<Integer> curLevel = new ArrayList<>();
            Stack<TreeNode> stack = new Stack<>();
            for (int i = 0; i < size; i++) {
                if (right) {
                    TreeNode node = queue.removeFirst();
                    curLevel.add(node.val);
                    if (node.left != null) {
                        stack.add(node.left);
                    }
                    if (node.right != null) {
                        stack.add(node.right);
                    }
                } else {
                    TreeNode node = queue.removeFirst();
                    curLevel.add(node.val);
                    if (node.right != null) {
                        stack.add(node.right);
                    }
                    if (node.left != null) {
                        stack.add(node.left);
                    }
                }
            }
            while (!stack.isEmpty()) {
                queue.addLast(stack.pop());
            }
            right = !right;
            res.add(curLevel);
        }
        return res;
    }

}