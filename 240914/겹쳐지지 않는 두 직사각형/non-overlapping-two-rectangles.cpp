#include <iostream>
using namespace std;
int N, M;
int board[5][5];
bool vis[5][5];
bool InRange(int x, int y){
    return 0 <= x && x < N && 0 <= y && y < M;
}
bool Makeable(int x, int y, int w, int h){
    for(int i = x ; i < x+h ; i++){
        for(int j = y ; j < y+w ; j++){
            if(!InRange(i,j)) return false;
            if(vis[i][j]) return false;
        }
    }
    return true;
}
int makeSqare(){
    int r_val = -999999999;
    for(int x = 0 ; x < N ; x++){
        for(int y = 0 ; y < M ; y++){
            if(vis[x][y]) continue;
            // cout << "### x: "<<x << " y: " << y <<" ###\n";
            for(int h = 1 ; h <= N ; h++){
                for(int w = 1 ; w <= M ; w++){
                    int sum2 = 0;
                    if(!Makeable(x,y,w,h)) continue;
                    // cout << "w: "<<w<<" h: " << h<<", ";
                    for(int nx = x ; nx < x+h ; nx++){
                        for(int ny = y ; ny < y+w ; ny++){
                            sum2 += board[nx][ny];
                        }
                    }
                    // cout << sum2 << '\n';
                    r_val = max(r_val, sum2);
                }
            }
        }
    }
    // cout <<'\n'<< r_val << '\n';
    return r_val;
}
int main() {
    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> board[i][j];
        }
    }
    int ans = -999999999;
    //좌표 순회
    for(int x = 0 ; x < N ; x++){
        for(int y = 0 ; y < M ; y++){
            //직사각형 가로세로 크기 순회
            for(int h = 1 ; h <= N ; h++){
                for(int w = 1 ; w <= M ; w++){
                    int sum1 = 0;
                    // 첫번째 직사각형
                    if(!Makeable(x,y,w,h)) continue;
                    // cout << "MAKEABLE FIRST SQUARE\n";
                    for(int nx = x ; nx < x+h ; nx++){
                        for(int ny = y ; ny < y+w ; ny++){
                            sum1 += board[nx][ny];
                            vis[nx][ny] = true;
                        }
                    }
                    // cout << "sum1: " << sum1<<'\n';
                    // 두번째 직사각형
                    int sum2 = makeSqare();
                    ans = max(ans, sum1+sum2);
                    for(int nx = x ; nx < x+h ; nx++){
                        for(int ny = y ; ny < y+w ; ny++){
                            vis[nx][ny] = false;
                        }
                    }

                }
            }
        }
    }
    cout << ans;
    return 0;
}