#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution (vector<int> &A)
{
    map<int, bool> occurs;
    size_t size = A.size()+1;

    for (int i = 0; i < size ; ++i)
    {
        if (A[i] > 0 ){
            occurs[A[i]-1]=true;
        }
    }

    for ( size_t i = 0; i < size ; ++i){
        if (occurs[i] == false)
            return i+1;
    }
}

int main(){
    int arr[] = {-1, -2, 3,4,1,7};
    size_t n = sizeof(arr)/sizeof(arr[0]);
    vector<int> a(arr, arr+n);

    std::cout << "solution: " << solution(a)  << std::endl;

}