class RandomListNode {
    int label;
    RandomListNode next = null;
    RandomListNode random = null;

    RandomListNode(int label) {
        this.label = label;
    }
}

public class Solution {
    public RandomListNode Clone(RandomListNode pHead) {
        // 极端情况，一定要写先出来
        if (pHead == null) {
            return null;
        }

        RandomListNode curNode = pHead;
        // 第 1 步：根据 next 指针复制出一个新旧合一的链表
        // 此时，奇数索引（从 1 开始计算）的结点是旧的结点，偶数索引的结点是新的结点
        RandomListNode nextNode;
        RandomListNode copyNode;
        while (curNode != null) {
            nextNode = curNode.next;
            copyNode = new RandomListNode(curNode.label);
            curNode.next = copyNode;
            copyNode.next = nextNode;
            curNode = nextNode;
        }

        // 第 2 步：根据旧结点 random 指针，给新结点的 random 指针做出正确的指向
        // 指针复位到起始结点
        curNode = pHead;
        while (curNode != null) {
            copyNode = curNode.next;
            nextNode = copyNode.next;
            // 特别注意
            // 特别注意
            // 特别注意：有的结点很可能 random 的指向为空（题目中明确说明）
            // 所以：只要遇到 next 引用的时候，一定要注意判断是否为空
            copyNode.random = curNode.random == null ? null : curNode.random.next;
            curNode = nextNode;
        }

        // 第 3 步：旧结点和新结点分离（拆分链表）
        curNode = pHead;
        RandomListNode res = pHead.next;
        while (curNode != null) {
            copyNode = curNode.next;
            nextNode = copyNode.next;
            // 恢复原始结点
            curNode.next = copyNode.next;
            // 恢复拷贝结点
            // 这里也要同样注意空指针的问题，克隆结点的最后一个结点的下一个结点是 null
            copyNode.next = copyNode.next == null ? null : copyNode.next.next;
            curNode = nextNode;
        }
        return res;
    }
}
