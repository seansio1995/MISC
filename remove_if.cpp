#include <iostream>
#include <algorithm>

bool isOdd(int num){
  return ((num%2)==1);
}
using namespace std;

int main(){
  int myints[]={1,2,3,4,5,6,7,8,9};
  int* begin=myints;
  int* end=myints+sizeof(myints)/sizeof(int);


  end=remove_if(begin,end,isOdd);

  for (int* p=begin;p!=end;++p){
    cout<<*p<<" ";
  }

  return 0;


}
