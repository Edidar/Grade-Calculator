#include<bits/stdc++.h>
#define pii pair<int,int>
#define M 10000
using namespace std;
int n,m,value,sx,sy,dx,dy,cnt=0;
int Grid[M][M],patcost[M][M];
map<pii,pii>parent;
bool vis[M][M];
int dxx[]={-1,0,+1,0};
int dyy[]={0,+1,0,-1};


void InitialState(){
    cin>>sx>>sy;
}

void GoalState()
{
    cin>>dx>>dy;
}

bool IsValid(int x,int y){
    if(x>=0 && x<n && y>=0 && y<m)
        return 1;
    return 0;
}

void Solution(int x,int y){
    pii p1,p2;
    cout<<"Current Path."<<endl;
    cout<<" Path : "<<x<<" "<<y<<endl;
    int n1,n2;
    p1.first = x, p1.second = y;
    while(1){
        p2 = parent[p1];
        if(p2.first==sx && p2.second==sy){
            cout<<" Path : "<<sx<<" "<<sy<<endl;
            return;
        }
        cout<<" Path : "<<p2.first<<" "<<p2.second<<endl;
        p1 = p2;
    }

}


void State(){

    queue<pii>q;
    pii fnt,child,p2;
    p2.first = -1, p2.second = -1;
    fnt.first = sx, fnt.second = sy;
    q.push(fnt);
    patcost[sx][sy] = 0;
    parent[fnt] = p2;

   // cout<<"Validation: "<<parent[fnt].first<<" "<<parent[fnt].second<<endl;
    while(!q.empty()){
        fnt = q.front();
        cnt++;
        q.pop();
        int xx = fnt.first, yy = fnt.second;
        //cout<<"Execute x: "<<xx<<" y: "<<yy<<endl;
        if(xx==dx && yy == dy){
            cout<<"Found solution."<<endl;
            cout<<"Total Path Cost: "<<patcost[dx][dy]<<endl;
            cout<<"Total Visit: "<<cnt<<endl;
            Solution(xx,yy);
            return;
        }

        for(int i=0;i<4;i++){
            int x = xx + dxx[i], y = yy + dyy[i];
            if(vis[x][y]) continue;
            if(IsValid(x,y)){
                if(Grid[x][y]==1)
                    continue;
                if(vis[x][y]==0){
                    vis[x][y] = 1;
                    patcost[x][y] = patcost[xx][yy] + 1;
                    child.first = x, child.second = y;
                    parent[child] = fnt;
                    q.push({x,y});
                }
            }
        }

    }



}

int main()
{
    memset(vis,0,sizeof(vis));
    cin>>n>>m;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>Grid[i][j];
        }
    }
    InitialState();
    GoalState();

    State();
    return 0;
}

/**

10 10

0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0
7 6


*/


