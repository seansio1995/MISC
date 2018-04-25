#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

double median(vector<int> b){
    int n=b.size();
    double m=b[n/2];
    if (!(n & 1))
    {
        m+=b[n/2-1];
        m/=2;
}


    return m;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin>>n;
    vector<int> a(n);
    vector<int> f(n);


    for (int i=0;i<n;i++)
    {
        cin>>a[i];
}

    for (int i=0;i<n;i++)
    {
        cin>>f[i];
}
    int total_nums=0;
    for (int i=0;i<n;i++)
    {
        total_nums+=f[i];
}
    vector<int> nums;


    for (int i=0;i<n;i++)
    {
        for (int j=0;j<f[i];j++){
            nums.push_back(a[i]);
}
}
    sort(nums.begin(),nums.end());
    vector<int> left;
    vector<int> right;

    if (total_nums & 1)
    {
        for(int i=0;i<total_nums/2;i++){
            left.push_back(nums[i]);
}

        for(int i=total_nums/2+1;i<total_nums;i++){
            right.push_back(nums[i]);
}
}
    else{
        for (int i=0;i<total_nums/2;i++)
        {
            left.push_back(nums[i]);
}

       for (int i=total_nums/2;i<total_nums;i++){
           right.push_back(nums[i]);
       }
    }

    double q1=median(left);
    double q3=median(right);
    double IQ=q3-q1;
    cout<<setprecision(1)<<fixed<<IQ<<endl;
    // for (int i=0;i<2;i++)
    // {
    //   cout<<nums[i]<<endl;
    // }

    //cout<<total_nums<<endl;
    return 0;
}
