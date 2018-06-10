#include <iostream>
using namespace std;

void BubbleSort(int* A, int l){
  int temp = 0;
  for(int i = 0; i < l; i++){
    for(int j = 0; j < l-1; j++){
      if(A[j] > A[j+1]){
        temp = A[j];
        A[j] = A[j+1];
        A[j+1] = temp;
      }
    }
  }
}

int main(){
  int A[5] = {5,4,3,2,1};
  int l = sizeof(A)/sizeof(int);
  BubbleSort(A, l);
  for(int i = 0; i < l; i++){
    cout << A[i] << endl;
  }
}
