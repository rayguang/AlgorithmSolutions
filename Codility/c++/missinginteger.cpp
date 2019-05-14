#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    size_t size = A.size() + 1;
    map<int, bool> occurs;

    for (size_t i = 0; i < size; ++i) {
        if (A[i] > 0 && A[i] <= A.size()) {
            // std::cout << "i: " << i << " A[i]: " << A[i] << "  A.size(): " << A.size() << std::endl;
            occurs[A[i] - 1] = true;
        }
    }

    for (auto it : occurs)
        std::cout << it.first+1 << " " << it.second << std::endl;

    for (size_t i = 0; i < size; ++i) {
        if (occurs[i] == false)
            return i + 1;
    }

    return 0;
}



int main ()
{
    int arr[] = { -1, -2, 0, 1, 2, 4, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    vector<int> a(arr, arr+n);
    for (int itr : a)
        std::cout << itr << std::endl;
    
    std::cout << solution(a) << std::endl;
}

