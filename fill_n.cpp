#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){

  vector<int> myvector(8,10);

  fill_n(myvector.begin(),4,20);
  fill_n(myvector.begin()+3,3,30);


  for (vector<int>::iterator it =myvector.begin();it!=myvector.end();++it){
    cout<<*it<<" ";
  }

  return 0;
}
