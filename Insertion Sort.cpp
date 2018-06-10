#include <iostream>
using namespace std;

void insertionSort(int* A, int l){
  int i = 0, key = 0;
  for(int j = 1; j < l; j++){
    key = A[j];
    i = j - 1;
    while(i >= 0 && A[i] > key){
      A[i+1] = A[i];
      A[i] = key;
      i--;
    }
  }
}

int main(){
  int A[5] = {5,4,3,2,1};
  int l = sizeof(A)/sizeof(int);
  insertionSort(A, l);
  for(int i = 0; i < l; i++){
    cout << A[i] << endl;
  }
}
