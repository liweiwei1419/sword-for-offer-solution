import java.util.LinkedList;

public class Solution {
    // 约瑟夫环问题
    // 其实并不一定要构造出一个真的循环链表
    public int LastRemaining_Solution(int n, int m) {
        // 这里用链表是为了提升性能，如果用 ArrayList 在删除操作中，就会有大量的性能消耗
        LinkedList<Integer> list = new LinkedList<>();
        int bt = 0;
        for (int i = 0; i < n; i++) {
            list.addLast(i);
        }
        while (list.size() > 1) {
            bt = (bt + m - 1) % list.size();
            list.remove(bt);
        }
        // 思考为什么会有最后这个判断
        return list.size() == 1 ? list.get(0) : -1;
    }
}