#include <iostream>
#include <string>
using namespace std;


int main(){
  string num=to_string(11120);
  int i=0;
  int res=0;
  while (i<num.length()){
    cout<<(int)num[i];
    res=res+(int)(num[i]);
    i++;
  }
  cout<<endl;
  cout<<res<<endl;
  return 0;
}
