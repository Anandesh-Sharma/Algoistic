public class RecursiveIS{
	public static void sort(int[] A, int n, int j){
		int i = 0, key = 0;
		if(j >= n)
			return;
		i = j - 1;
		key = A[j];
		while(i >= 0 && A[i] > key){
			A[i+1] = A[i];
			A[i] = key;
			i--;
		}
		sort(A, n, j + 1);
	}

	public static void main(String...args){
		int[] A = {0,9,8,7,6,5,4,3,2,1};

		RecursiveIS.sort(A, A.length, 0);

		for(int i = 0; i < A.length; i++){
			System.out.print(A[i] + " ");
		}
	}
}


