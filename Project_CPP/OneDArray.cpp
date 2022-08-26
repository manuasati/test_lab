#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

bool hasNegativeIntegers(const int arr[], int size)
{
    bool result = false;
    for(int i=0; i<size; i++)
    {
        if(arr[i] < 0)
        {
            result = true;
            break;
        }
    }

    return result;
}

bool hasOddIntegers(const int arr[], int size)
{
    bool result = false;
    for(int i=0; i<size; i++)
    {
        if(arr[i]%2 != 0)
        {
            result = true;
            break;
        }
    }

    return result;
}

bool isInOrder(const int arr[], int size)
{
    if(size == 0 || size == 1)
    {
        return true;
    }

    bool result = true;
    for(int i=1; i<size; i++)
    {
        if(arr[i-1] > arr[i])
        {
            result = false;
            break;
        }
    }

    return result;
}

/* Utility function to print an array */
void printArray(int arr[], int size) 
{ 
    for (int i = 0; i < size; i++) 
        cout << arr[i] << " "; 
  
    cout << endl; 
}

//Utility function to swap two numbers
void swap(int& first, int& second)
{
    int temp = first;  
    first = second; 
    second = temp;     
}

void inverseArray(int arr[], int size)
{
    int start = 0;
    int end = size-1;
    while (start < end) 
    { 
        swap(arr[start], arr[end]); 
        start++; 
        end--; 
    }
}

void randomizeArray(int arr[], int size)
{
    // Use a different seed value so that we don't get same 
    // result each time we run this program 
    srand ( time(NULL) ); 

    for (int i=size-1; i>0; i--) 
    { 
        // Pick a random index from 0 to i 
        int j = rand() % (i+1); 

        // Swap arr[i] with the element at random index 
        swap(arr[i], arr[j]); 
    }
}


int main()
{
    int arr[] = { 1, 5, 5, 5, -4, 2 }; 
    int arr1[] = { 1, 5, 15, 25, 34, 42 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int n1 = sizeof(arr1) / sizeof(arr1[0]);

    cout << "Whether the array has negetive integers: " << hasNegativeIntegers(arr, n) << endl;
    cout << "Whether the array has odd integers: " << hasOddIntegers(arr, n) << endl;
    cout << "Whether the array has elements in orded: " << isInOrder(arr1, n1) << endl;

    cout << "Array Elements Before reversing: " << endl;
    printArray(arr1, n1);
    inverseArray(arr1, n1);
    cout << "Array Elements After reversing: " << endl;
    printArray(arr1, n1);

    cout << "Array Elements Before randomizing: " << endl;
    printArray(arr1, n1);
    randomizeArray(arr1, n1);
    cout << "Array Elements After randomizing: " << endl;
    printArray(arr1, n1);

    return 0;
}
