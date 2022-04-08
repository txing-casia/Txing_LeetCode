#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
private:
    unordered_map<char, int> symbolValues = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000},
    };

public:
    int romanToInt(string s) {
        int ans = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            int value = symbolValues[s[i]];
            if (i < n - 1 && value < symbolValues[s[i + 1]]) {
                ans -= value;
            } else {
                ans += value;
            }
        }
        return ans;
    }
};

int main()
{
    Solution S; 
    char a[3] = "IX";
    cout << S.romanToInt(a);
    system("pause");
    return 0;
}








// #include <iostream>
// // using namespace std;
// int main()
// { //[1,1,2,3,4,5,6,7,1,2]
//     int a[10]={1,2,3,4,5,6,7,8,9,10};
//     a[2]=1;
//     // std::cout << a <<std::endl;
//     std::cout << a[1] <<std::endl;
//     std::cin >> a[2];
//     printf("%d",a[3]);
//     // scanf("%s",name);
//     return a[1];
// } 



