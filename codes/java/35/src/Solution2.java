/**
 * 同 Solution，来自参考解答
 */
public class Solution2 {
    public RandomListNode Clone(RandomListNode pHead) {
        if (pHead == null) {
            return null;
        }
        RandomListNode currentNode = pHead;
        //1、复制每个结点，如复制结点 A 得到 A1，将结点 A1 插到结点 A 后面；
        while (currentNode != null) {
            RandomListNode cloneNode = new RandomListNode(currentNode.label);
            RandomListNode nextNode = currentNode.next;
            currentNode.next = cloneNode;
            cloneNode.next = nextNode;
            currentNode = nextNode;
        }
        currentNode = pHead;
        //2、重新遍历链表，复制老结点的随机指针给新结点，如 A1.random = A.random.next;
        while (currentNode != null) {
            currentNode.next.random = currentNode.random == null ? null : currentNode.random.next;
            currentNode = currentNode.next.next;
        }
        //3、拆分链表，将链表拆分为原链表和复制后的链表
        currentNode = pHead;
        RandomListNode pCloneHead = pHead.next;
        while (currentNode != null) {
            RandomListNode cloneNode = currentNode.next;
            // 恢复出原始结点的 next 指向
            currentNode.next = cloneNode.next;
            // 除了最后一个克隆的结点，其余克隆结点都有下一个结点的下一个结点，所以这里要做空指针判断
            cloneNode.next = cloneNode.next == null ? null : cloneNode.next.next;
            currentNode = currentNode.next;
        }
        return pCloneHead;
    }


    public static void main(String[] args) {

    }
}
