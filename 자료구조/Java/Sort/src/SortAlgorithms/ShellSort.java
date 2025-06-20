package SortAlgorithms;

import java.util.Arrays;

public class ShellSort {
    public static void main(String[] args){
        int[] arr = {4,6,9,1,5,3};
        ShellSort(arr);
    }

    public static void ShellSort(int[] arr) {
        int d = arr.length;
        while(d > 1){
            d = d/2;
            if (d % 2 == 0) {
                d = d+1;
            }

            for (int i=0; i<d; i++){
                int count = 0;
                int val = i;
                while (val < arr.length) {
                    val = val+d;
                    count++;
                }
                int[] temp = new int[count];
                for (int j = 0; j<count; j++) {
                    temp[j] = arr[i+j*d];
                }
                int[] sortTemp = insertSort(temp);
                for (int k = 0; k<count; k++) {
                    arr[i+k*d] = sortTemp[k];
                }
            }
            System.out.println(Arrays.toString(arr));
        }
    }

    public static int[] insertSort(int[] arr) {
        for (int i=1; i<arr.length; i++){
            int temp = arr[i];
            int prev = i-1;
            while(prev>=0 && arr[prev]>temp){
                arr[prev+1] = arr[prev];
                prev--;
            }
            arr[prev+1] = temp;
        }
        return arr;
    }
}
