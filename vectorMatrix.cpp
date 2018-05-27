#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int main(){
	int RR,CC;
	cin>>RR;
	cin>>CC;
	vector<vector<int> > matrix(RR,vector<int>(CC));
	for(int i=0;i<RR;i++){
		for (int j=0;j<CC;j++){
			cin>>matrix[i][j];
		}
	}
	for(int i=0;i<matrix.size();i++){
		for(int j=0;j<matrix[0].size();j++){
			cout<<matrix[i][j];
		}
	}
	return 0;
}
