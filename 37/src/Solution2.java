import java.util.LinkedList;

class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}

// 前序遍历
public class Solution {


    String Serialize(TreeNode root) {
        StringBuilder stringBuilder = new StringBuilder();
        preOrder(root, stringBuilder);
        return stringBuilder.toString();
    }

    private void preOrder(TreeNode node, StringBuilder stringBuilder) {
        if (node == null) {
            stringBuilder.append("#");
            stringBuilder.append(",");
            return;
        }
        stringBuilder.append(node.val);
        stringBuilder.append(",");
        preOrder(node.left, stringBuilder);
        preOrder(node.right, stringBuilder);
    }

    TreeNode Deserialize(String str) {
        String[] strings = str.split(",");
        int size = strings.length;
        System.out.println(size);
        LinkedList<String> queue = new LinkedList<>();
        for (int i = 0; i < size; i++) {
            queue.addLast(strings[i]);
        }
        return inOrderGenerate(queue);
    }

    private TreeNode inOrderGenerate(LinkedList<String> queue) {
        if (queue.isEmpty()) {
            return null;
        }
        String s = queue.removeFirst();
        if (!"#".equals(s)) {
            TreeNode root = new TreeNode(Integer.parseInt(s));
            root.left = inOrderGenerate(queue);
            root.right = inOrderGenerate(queue);
            return root;
        }
        return null;
    }


    public static void main(String[] args) {
        TreeNode node8 = new TreeNode(8);
        TreeNode node6 = new TreeNode(6);
        TreeNode node10 = new TreeNode(10);
        TreeNode node5 = new TreeNode(5);
        TreeNode node7 = new TreeNode(7);
        TreeNode node9 = new TreeNode(9);
        TreeNode node11 = new TreeNode(11);

        node8.left = node6;
        node8.right = node10;

        node6.left = node5;
        node6.right = node7;

        node10.left = node9;
        node10.right = node11;

        Solution solution = new Solution();
        String serialize = solution.Serialize(node8);
        System.out.println(serialize);

        solution.Deserialize("8,6,5,#,#,7,#,#,10,9,#,#,11,#,#,");
    }
}