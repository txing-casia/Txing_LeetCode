#include <iostream>
#include <string.h>
using namespace std;

int maximalSquare(matrix){
    int m = matrix.size(),n = matrix[0].size();
    int f[m][n];
    int ans = 0;

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            f[i][j]=0;
        }
    }

    for(int i = 0;i < m;i++){
        for(int j = 0;j < n;j++){
            if(i==0 or j==0){
                f[i][j] = matrix[i][j];
            }
            else if(matrix[i][j] == 0){
                f[i][j] = 0;
            }
            else{
                f[i][j] = min(f[i-1][j-1],min(f[i-1][j],f[i][j-1]))+1;
            }
            ans += f[i][j];
        }
    }
    return ans;
}

int main(){
    int ans = 0;
    char matrix[4][5] = {{'1','0',"1","0","0"},{"1","0","1","1","1"},{"1","1","1","1","1"},{"1","0","0","1","0"}};

    // int m = matrix.size(),n = matrix[0].size();
    // int f[m][n];
    // int ans = 0;

    // for(int i=0;i<m;i++){
    //     for(int j=0;j<n;j++){
    //         f[i][j]=0;
    //     }
    // }

    // for(int i = 0;i < m;i++){
    //     for(int j = 0;j < n;j++){
    //         if(i==0 or j==0){
    //             f[i][j] = int(matrix[i][j]);
    //         }
    //         else if(matrix == 0){
    //             f[i][j] = 0;
    //         }
    //         else{
    //             f[i][j] = min(f[i-1][j],f[i][j-1],f[i-1][j-1])+1;
    //         }
    //         ans += f[i][j];
    //     }
    // }
    // return ans;



    return 0;
}
