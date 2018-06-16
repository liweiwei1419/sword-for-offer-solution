import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * 使用 Hash 表的方式
 *
 * @author liwei
 */
public class Solution3 {
    public RandomListNode Clone(RandomListNode pHead) {
        Map<RandomListNode, RandomListNode> map = new HashMap<>();
        RandomListNode curNode = pHead;
        // 体会这里设置虚拟头结点的必要性
        RandomListNode dummyNode = new RandomListNode(-1);
        RandomListNode p = dummyNode;
        // 完成复制 next 结点，并且将对应关系放入 Hash 表
        while (curNode != null) {
            RandomListNode newNode = new RandomListNode(curNode.label);
            map.put(curNode, newNode);
            curNode = curNode.next;
            p.next = newNode;
            p = newNode;
        }
        // 完成复制链表的 random 指针的赋值
        Set<Map.Entry<RandomListNode, RandomListNode>> entrySet = map.entrySet();
        for (Map.Entry<RandomListNode, RandomListNode> entry : entrySet) {
            entry.getValue().random = map.get(entry.getKey().random);
        }
        return dummyNode.next;
    }
}
