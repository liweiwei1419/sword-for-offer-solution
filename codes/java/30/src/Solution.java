import java.util.Stack;

public class Solution {

    private Stack<Integer> minStack = new Stack<>();
    private Stack<Integer> dataStack = new Stack<>();

    public void push(int node) {
        if (minStack.isEmpty()) {
            minStack.push(node);
            dataStack.push(node);
            return;
        }
        int curMin = minStack.peek();
        if (node < curMin) {
            minStack.push(node);
        } else {
            minStack.push(curMin);
        }
        dataStack.push(node);
    }

    public void pop() {
        minStack.pop();
        dataStack.pop();
    }

    public int top() {
        return dataStack.pop();
    }

    public int min() {
        return minStack.peek();
    }
}