#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool smaller(int i,int j){
  return (i<j);
}

struct myclass {
  bool operator() (int i,int j){
    return (i<j);
  }


} myobject;


int main(){
  int myints[]={32,71,12,45,26,80,53,33};

  vector<int> myvector(myints,myints+8);

  sort(myvector.begin(),myvector.begin()+4,smaller);
  sort(myvector.begin()+4,myvector.end(),myobject);

  sort( myvector.begin(),myvector.end());

  for(vector<int>::iterator it=myvector.begin();it!=myvector.end();++it){
    cout<<*it<<" ";
  }

  return 0;
}
