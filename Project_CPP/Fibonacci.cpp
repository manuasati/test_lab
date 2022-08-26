#include<iostream>
#include<stdlib.h>
#include<cmath> 

using namespace std;

// A utility function that returns true if x is perfect square 
bool isPerfectSquare(int x) 
{ 
    int s = sqrt(x); 
    return (s*s == x); 
} 

bool containsFibonacciSeries(const int arr[], const int size)
{
    bool result = true;
    cout << "The integers in the table are : " << endl;
    for(int i=0; i<size; i++)
    {
        int n = arr[i];
        cout << "element #" << i << ":" << arr[i] << endl;
        if(result)
        {
            result = isPerfectSquare(5*n*n + 4) || isPerfectSquare(5*n*n - 4); 
        }
    }

    return result;
}

int main()
{
    cout << "This program determines whether an array contains the FIBONNACI series." << endl;
    int arr1[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 };
    int n = sizeof(arr1) / sizeof(arr1[0]);    
    bool result = containsFibonacciSeries(arr1, n);    
    if(result)
    {cout << "The board contains the Fibonacci series." << endl;}
    else
    {cout << "The table doesn’t contain the Fibonacci series." << endl;}

    int arr2[] = { 0, 1, 1, 2, 3, 6, 8, 13, 21, 34 };
    n = sizeof(arr2) / sizeof(arr2[0]);    
    result = containsFibonacciSeries(arr2, n);    
    if(result)
    {cout << "The board contains the Fibonacci series." << endl;}
    else
    {cout << "The table doesn’t contain the Fibonacci series." << endl;}

    return 0;
}
