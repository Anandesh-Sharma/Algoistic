public class Selection_Sort{
	public static void main(String...args){
		int[] A = {2,1,3,5,4};
		int swap = 0;

		for(int i = 0; i < A.length; i++){
			for(int j = i; j < A.length; j++){
				if(A[i] > A[j]){
					swap = A[i];
					A[i] = A[j];
					A[j] = swap;
				}
			}
		}

		for(int k = 0; k < A.length; k++)
			System.out.print(A[k] + " ");
	}
}
