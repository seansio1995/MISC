#include "queueByStack.h"
#include <iostream>

using namespace std;

class queueByStack{
private:
  stack<int> inStack;
  stack<int> outStack;

public:
  void enqueue(int ele){
    inStack.push(ele);
  }


  int dequeue(){
    if(outStack.empty()){
      while (!inStack.empty()){
        int newEle=inStack.top();
        inStack.pop();
        outStack.push(newEle);
      }

    }

    if (outStack.empty()){
      throw runtime_error("Can't deque from the queue");
    }

    int result=outStack.top();
    outStack.pop();
    return result;
  }
};


int main(){
  queueByStack myQueue;
  myQueue.enqueue(1);
  myQueue.enqueue(2);
  myQueue.enqueue(3);

  cout<<myQueue.dequeue()<<endl;
  cout<<myQueue.dequeue()<<endl;
  cout<<myQueue.dequeue()<<endl;
  return 0;
}
