#include <iostream>     // std::cout
#include <algorithm>    // std::generate
#include <vector>       // std::vector
#include <ctime>        // std::time
#include <cstdlib>      // std::rand, std::srand

using namespace std;

int randomNumber (){
  return (rand()%100);
}


struct c_unique {
  int current;
  c_unique() {current=0;}
  int operator()() {return ++current;}
} UniqueNumber;


int main(){
  vector<int> myvec(8);
  generate(myvec.begin(),myvec.end(),randomNumber);

  for (vector<int>:: iterator it=myvec.begin();it!=myvec.end();++it){
    cout<<*it<<" ";
  }

  cout<<endl;

  generate(myvec.begin(),myvec.end(),UniqueNumber);

  for (vector<int>:: iterator it=myvec.begin();it!=myvec.end();++it){
    cout<<*it<<" ";
  }

  return 0;
}
