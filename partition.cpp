#include <iostream>     // std::cout
#include <algorithm>    // std::partition
#include <vector>       // std::vector

using namespace std;
bool IsOdd (int i) { return (i%2)==1; }

int main () {
vector<int> myvector;

  // set some values:
  for (int i=1; i<10; ++i) myvector.push_back(i); // 1 2 3 4 5 6 7 8 9

  vector<int>:: iterator bound;
  bound=partition(myvector.begin(),myvector.end(),IsOdd);

  cout<<"Odd numbers:"<<endl;

  for(vector<int>::iterator it=myvector.begin();it!=bound;++it){
    cout<<*it<<" ";
  }

  cout<<endl;
  cout<<"Even numbers:"<<endl;
  for(vector<int>::iterator it=bound;it!=myvector.end();++it){
    cout<<*it<<" ";
  }

  return 0;
}
