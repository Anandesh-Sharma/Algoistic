public class Bubble_Sort{
	public static void main(String...args){
		//array
		int[] A = {0,9,8,7,6,5,4,3,2,1};
		int swap = 0;

		for(int i = 0; i < A.length; i++){
			for(int j = 0; j < A.length - 1; j++){
				if(A[j] > A[j+1]){
					swap = A[j];
					A[j] = A[j+1];
					A[j+1] = swap;
				}
			}
		}
		for(int k = 0; k < A.length; k++){
			System.out.print(A[k] + " ");
		}
	}
}
