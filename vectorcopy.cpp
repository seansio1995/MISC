#include <vector>
#include <iostream>
using namespace std;


int main(){
  vector<int> vec1{1,2,3};
  vector<int> vec2{2,3,4};

  vec2.assign(vec1.begin(),vec1.end());

  for (int i=0;i<vec2.size();i++){
    cout<<vec2[i]<<" ";
  }
  return 0;
}
