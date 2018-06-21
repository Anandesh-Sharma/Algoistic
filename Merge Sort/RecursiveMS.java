public class RecursiveMS{

	public static void merge(int[] L, int[] R, int [] A){
		int i = 0, j = 0, k = 0;
		while(i < L.length && j < R.length){
			if(L[i] < R[j]){
				A[k] = L[i];
				i++;
			}
			else{
				A[k] = R[j];
				j++;
			}
			k++;
		}
		//if one of the subarray exhausted
		while(i < L.length){
			A[k] = L[i];
			i++; 	k++;
		}

		while(j < R.length){
			A[k] = R[j];
			j++; 	k++;
		}

	}

	public static void mergeSort(int[] A){
		int n = A.length;
		if(n < 2)
			return;
		int middle = n/2;
		int[] L = new int[middle];
		int[] R = new int[n - middle];
		for(int i = 0; i < middle; i++)
			L[i] = A[i];

		for(int j = middle; j < n; j++)
			R[j - middle] = A[j];

		mergeSort(L);
		mergeSort(R);
		merge(L,R,A);
	}

	public static void main(String...args){
		int [] A = {2,1,4,6,8,7,3,5};
		RecursiveMS.mergeSort(A);
		for(int i = 0; i < A.length; i++)
			System.out.print(A[i] + " ");
	}
}

