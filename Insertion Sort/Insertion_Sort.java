public class Insertion_Sort{
	public static void main(String...args){
		//array
		int[] A = {0,9,8,7,6,5,4,3,2,1};
		int i = 0, key = 0;

		for(int j = 0; j < A.length; j++){
			i = j - 1;
			key = A[j];
			while(i >= 0 && A[i] > key){
				A[i+1] = A[i];
				A[i] = key;
				i = i - 1;
			}
		}

		for(int j = 0; j < A.length; j++){
			System.out.print(A[j] + " ");
		}
	}
}

