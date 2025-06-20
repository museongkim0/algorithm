package SortAlgorithms;

import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args) {
        int[] arr = {4,6,9,1,5,3};
        bubbleSort(arr);
    }

    public static void bubbleSort(int[] arr){
        int n = arr.length;
        for (int i = 0; i < n-1; i++){
            for (int j = 0; j < n-1-i; j++){
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
            System.out.println(Arrays.toString(arr));
        }
    }
}