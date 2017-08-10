#include <iostream>
#include <queue>


using namespace std;

int main(){

  priority_queue<int> mypq;
  mypq.push(30);
  mypq.push(100);
  mypq.push(25);
  mypq.push(40);


  while(!mypq.empty()){
    cout<<mypq.top()<<endl;
    mypq.pop();
  }

  return 0;
}
