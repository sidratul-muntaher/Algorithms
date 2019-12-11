



#include<iostream>
using namespace std;
#include<cmath>

int binary(int arr[],int item)
{
    int low = 0;
    int high = 9999; // [ Problem ] if
    int mid;
    for(int low = 0; low <= high; )
    {
        mid = round((high + low)/2);
        if(arr[mid] == item)
        {
            return mid;
        }
        else if(arr[mid] < item)
        {
            low = mid + 1;
        }
        else if(arr[mid] > item)
        {
            high = mid - 1;
        }
        else
            return 0;
    }
    if(high > low)
    {
        return 0;
    }

}

main()
{
    int x[10000];
    for(int i = 0, j = 3; i<10000; i++, j = j+2)
    {
        x[i] = j;
    }
    for(int i = 0 ; i <10000; i++)
    {
       // cout <<"index ["<< i << "] = "<< x[i]<< endl;
    }
    cout << binary(x, 19991);
}
