// implementation of bubble sort in c++
#include <iostream>
using namespace std;


int main(){
  int size;
  cout<<"Enter the size of array:"<<endl;
  cin>>size;
  int A[size];
  for (int i=0;i<size;i++){
    cout<<"Enter the number:";
    cin>>A[i];
    //cout<<endl;
  }

  cout<<endl;
  cout<<"Print out the original array"<<endl;
  for (int i=0;i<size;i++){
    cout<<A[i]<<" ";
  }

  //bubble sort
  int tmp;
  for (int i=0;i<size;i++){
    for (int j=size-1;j>i;j--){
      if (A[j]< A[j-1]){
        tmp=A[j];
        A[j]=A[j-1];
        A[j-1]=tmp;
      }
    }
  }

  cout<<"Print out the array after sorting"<<endl;
  for (int i=0;i<size;i++){
    cout<<A[i]<<" ";
  }
  return 0;
}
