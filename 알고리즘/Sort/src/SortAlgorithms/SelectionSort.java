package SortAlgorithms;

import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args){
        int[] arr = {4,6,9,1,5,3};
        selectionSort(arr);
    }

    public static void selectionSort(int[] arr){
        for(int i=0; i<arr.length; i++){
            int minIndex = i;
            for(int j=i+1; j<arr.length; j++){
                if(arr[minIndex] > arr[j]) {
                    minIndex = j;
                }
            }
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
            System.out.println(Arrays.toString(arr));
        }
    }
}
