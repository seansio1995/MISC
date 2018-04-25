#include <iostream>
using namespace std;

class A {
  int x;
public:
  A() {
    x=0;
    x++;
  }
};



int main(){
  for(int i=0;i<100;i++){
    A *a=new A();
    delete a;
  }

  cout<<"Ding"<<endl;
  return 0;
}
