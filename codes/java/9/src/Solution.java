import java.util.Stack;

public class Solution {
    /**
     * 专门 push 的时候用
     */
    private Stack<Integer> stack1 = new Stack<Integer>();
    /**
     * 专门 pop 的时候用
     */
    private Stack<Integer> stack2 = new Stack<Integer>();

    private State lastState = State.PUSH;

    enum State {
        PUSH, POP
    }

    public void push(int node) {
        if (lastState == State.PUSH) {
            stack1.add(node);
        } else {
            assert lastState == State.POP;
            // 如果上一步是 pop 的话，
            while (!stack2.isEmpty()) {
                stack1.add(stack2.pop());
            }
            stack1.add(node);
            lastState = State.PUSH;
        }
    }

    public int pop() {
        if (lastState == State.POP) {
            if (stack2.empty()) {
                throw new IllegalArgumentException("queue is empty");
            }
            return stack2.pop();
        } else {
            // 如果上一步是 PUSH 的话
            while (!stack1.empty()) {
                stack2.add(stack1.pop());
            }
            lastState = State.POP;
            return stack2.pop();
        }
    }
}