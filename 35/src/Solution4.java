public class Solution4 {

    // Python 写法能够通过
//    class Solution:
//            # 返回 RandomListNode
//    def Clone(self, pHead):
//            # write code here
//        if not pHead: return
//    newNode = RandomListNode(pHead.label)
//    newNode.random = pHead.random
//    newNode.next = self.Clone(pHead.next)
//            return newNode

    // 不能通过
    public RandomListNode Clone(RandomListNode pHead) {
        if (pHead == null) {
            return null;
        }
        RandomListNode p = new RandomListNode(pHead.label);
        p.next = pHead.next;
        p.random = pHead.random;
        if(pHead.next!=null){
            p.next = Clone(pHead.next);
        }
        return p;
    }





}
