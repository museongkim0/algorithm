import org.example.stack.ListBasedStack;
import org.junit.Test;
import java.util.Random;
import java.util.Stack;

import static org.junit.Assert.*;

public class StackTest {
    private static final int NUM_OPERATIONS = 1_000_000;
    private static final Random random = new Random();

    @Test
    public void testRandomOperations() {
        Stack<Integer> referenceStack = new Stack<>();
        ListBasedStack<Integer> testStack = new ListBasedStack<>();

        String[] operations = {"push", "pop", "peek", "empty", "size"};

        for (int i = 0; i < NUM_OPERATIONS; i++) {
            String op = operations[random.nextInt(operations.length)];

            if ((op.equals("pop") || op.equals("peek")) && referenceStack.empty()) {
                continue;
            }

            try {
                switch (op) {
                    case "push" -> {
                        int value = random.nextInt(2001);
                        referenceStack.push(value);
                        testStack.push(value);
                    }
                    case "pop" -> {
                        int refVal = referenceStack.pop();
                        int testVal = testStack.pop();
                        assertEquals(refVal, testVal);
                    }
                    case "peek" -> {
                        int refVal = referenceStack.peek();
                        int testVal = referenceStack.peek();
                        assertEquals(refVal, testVal);
                    }
                    case "empty" -> {
                        boolean refVal = referenceStack.empty();
                        boolean testVal = testStack.empty();
                        assertEquals(refVal, testVal);
                    }
                    case "size" -> {
                        int refVal = referenceStack.size();
                        int testVal = testStack.size();
                        assertEquals(refVal, testVal);
                    }
                }
            } catch (Exception e) {
                fail("Operation '" + op + "' failed: " + e.getMessage());
            }
        }
    }
}