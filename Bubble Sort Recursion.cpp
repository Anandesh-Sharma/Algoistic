#include <iostream>
using namespace std;

void BubbleSort(int* A, int l){
  if(l == -1){
    return;
  }
  int temp;
    for(int j = 0; j < l-1; j++){
      if(A[j] > A[j+1]){
        temp = A[j];
        A[j] = A[j+1];
        A[j+1] = temp;
      }
    }
    BubbleSort(A, l-1);
}

int main(){
  int A[5] = {5,4,3,2,1};
  int l = sizeof(A)/sizeof(int);
  BubbleSort(A, l);
  for(int i = 0; i < l; i++){
    cout << A[i] << endl;
  }
}
