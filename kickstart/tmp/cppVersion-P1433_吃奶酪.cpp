#include<stdio.h>
#include<vector>
#include<math.h>

using namespace std;



class XY
{
public:
    int x;
    int y;

    XY(int ix,int iy)
    {
        x=ix;
        y=iy;
    }

};

vector<XY> cheses;
vector<int> ispassed;
int n;
double result = 2000;


int iscomplete()
{
    for(int i=1;i<n+1;i++)
        {
            if(ispassed[i]==0)
            {
                return 0;
            }
        }
    return 1;
}

int dfs(int pre,double dis)
{
    if(dis>result) return 0;

    if(iscomplete())
    {
        if(result>dis)
        {
            result = dis;
        }
    }

    
    for(int i=1;i<n+1;i++)
    {
        if(ispassed[i]==0)
        {
            int x1 = cheses[pre].x;
            int y1 = cheses[pre].y;
            int x2 = cheses[i].x;
            int y2 = cheses[i].y;

            double tmpdis = dis+sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));

            ispassed[i]=1;
            dfs(i,tmpdis);
            ispassed[i]=0;

        }
    }

    return 0;
}


int main(int argc, char const *argv[])
{
    
    
    XY tmp(0,0);
    cheses.push_back(tmp);
    ispassed.push_back(1);

    
    scanf("%d",&n);
    for (int i = 1; i <n+1; ++i)
    {
        scanf("%d %d",&tmp.x,&tmp.y);
        cheses.push_back(tmp);
        ispassed.push_back(0);

    }
    

    dfs(0,0);

    //result+=0.005;
    printf("%.2f\n",result);
    return 0;
}
