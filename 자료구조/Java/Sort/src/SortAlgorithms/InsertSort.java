package SortAlgorithms;

import java.util.Arrays;

public class InsertSort {
    public static void main(String[] args){
        int[] arr = {4,6,9,1,5,3};
        insertSort(arr);
    }

    public static void insertSort(int[] arr) {
        for (int i=1; i<arr.length; i++){
            int temp = arr[i];
            int prev = i-1;
            while(prev>=0 && arr[prev]>temp){
                arr[prev+1] = arr[prev];
                prev--;
            }
            arr[prev+1] = temp;
            System.out.println(Arrays.toString(arr));
        }
    }
}
