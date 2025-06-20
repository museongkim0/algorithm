package SortAlgorithms;

import java.util.Arrays;

public class QuickSort {
    public static void main(String[] args){
        int[] arr = {4,6,9,1,5,3};
        quickSort(arr, 0, arr.length-1);
    }

    public static void quickSort(int[] arr, int left, int right){
        if(left >= right) return;
        System.out.println(Arrays.toString(arr));

        int pivot = partition(arr, left, right);

        quickSort(arr, left, pivot-1);
        quickSort(arr, pivot+1, right);
    }

    public static int partition(int[] arr, int left, int right){
        int mid = (left+right)/2;
        swap(arr, left, mid);

        int l = left;
        int h = right;
        int pivot = arr[left];

        while (l < h){
            while(pivot < arr[h]){
                h--;
            }
            while(l < h && pivot >= arr[l]){
                l++;
            }
            swap(arr, l, h);
        }
        swap(arr, left, l);
        return l;
    }

    public static void swap(int[] arr, int l, int h){
        int temp = arr[l];
        arr[l] = arr[h];
        arr[h] = temp;
    }
}
