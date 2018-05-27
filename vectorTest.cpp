#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main(){
	vector<int> v;
	for (int i=0;i<10;i++){
		v.push_back(i);
		}
	if(find(v.begin(),v.end(),11)!=v.end()){
		cout<<"11 is found"<<endl;
	}
	else{
		cout<<"11 is not found"<<endl;
	}
	return 0;
}
