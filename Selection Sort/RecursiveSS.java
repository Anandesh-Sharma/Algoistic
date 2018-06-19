public class RecursiveSS{
	public static void sort(int[] A, int n, int i, int j){
		int swap;
		if(i >= n - 1)
			return;
		if(j < n){
			sort(A, n, i, j+1);
			if(A[i] > A[j]){
				swap = A[i];
				A[i] = A[j];
				A[j] = swap;
			}
		}
		if(j == 0)
			sort(A, n , i+1, i+1);
	}
	public static void main(String...args){
		int[] A = {2,1,3,5,4};
		sort(A, A.length, 0 , 0);

		for(int i = 0; i < A.length; i++)
			System.out.print(A[i] + " ");
	}
}


