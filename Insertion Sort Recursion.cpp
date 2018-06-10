#include <iostream>
using namespace std;

void insertionSort(int* A, int l, int j){
  if(j == l){
    return;
  }
  int i = 0, key = 0;
    key = A[j];
    i = j - 1;
    while(i >= 0 && A[i] > key){
      A[i+1] = A[i];
      A[i] = key;
      i--;
    }
    insertionSort(A, l, j+1);
}

int main(){
  int A[5] = {3,4,5,1,2};
  int l = sizeof(A)/sizeof(int);
  insertionSort(A, l, 1);
  for(int i = 0; i < l; i++){
    cout << A[i] << endl;
  }
}
