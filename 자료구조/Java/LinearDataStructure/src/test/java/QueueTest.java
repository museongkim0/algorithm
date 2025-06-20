import org.example.Queue.ArrayQueue;
import org.junit.Test;

import java.util.*;

import java.util.Queue;

import static org.junit.Assert.*;

public class QueueTest {
    private static final int NUM_OPERATIONS = 1_000_000;
    private static final Random random = new Random();

    @Test
    public void testRandomOperations() {
        Queue<Integer> referenceQueue = new LinkedList<>();
        ArrayQueue<Integer> testQueue = new ArrayQueue<Integer>();

        String[] operations = {"push", "pop", "front", "empty", "size"};

        for (int i = 0; i < NUM_OPERATIONS; i++) {
            String op = operations[random.nextInt(operations.length)];

            if ((op.equals("pop") || op.equals("front")) && referenceQueue.isEmpty()) {
                continue;
            }

            try {
                switch (op) {
                    case "push" -> {
                        int value = random.nextInt(2001) - 1000; // -1000 ~ 1000
                        referenceQueue.offer(value);
                        testQueue.push(value);
                    }
                    case "pop" -> {
                        int refVal = referenceQueue.poll();
                        int testVal = testQueue.pop().get();
                        assertEquals(refVal, testVal);
                    }
                    case "front" -> {
                        int refVal = referenceQueue.peek();
                        int testVal = testQueue.front().get();
                        assertEquals(refVal, testVal);
                    }
                    case "empty" -> {
                        boolean refVal = referenceQueue.isEmpty();
                        boolean testVal = testQueue.isEmpty();
                        assertEquals(refVal, testVal);
                    }
                    case "size" -> {
                        int refVal = referenceQueue.size();
                        int testVal = testQueue.getSize();
                        assertEquals(refVal, testVal);
                    }
                }
            } catch (Exception e) {
                fail("Operation '" + op + "' failed: " + e.getMessage());
            }
        }
    }
}
