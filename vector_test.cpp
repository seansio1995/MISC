#include <vector>
#include <iostream>
using namespace std;

int main()
{
  vector<int> nums(10);
  nums.push_back(1);
  nums.push_back(2);
  cout<<nums.size()<<endl;
  return 0;
}
