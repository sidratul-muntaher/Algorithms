#include<iostream>
using namespace std;
main()
{
    int x[10000]
    ;
    for(int i = 0, j = 3; i<10000; i++, j = j+2)
    {
        x[i] = j;
    }
    for(int i = 0; i < 10000; i++){
         if(x[i] == 19991)
    {
        cout << "found"<<endl;
    }
    }

}
