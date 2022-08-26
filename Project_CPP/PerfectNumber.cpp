#include<iostream>
#include<stdlib.h>
#include<cmath>
#include<sstream>
#include<vector>

using namespace std;

bool validateInputNumber(int x)
{
    if(x < 0 || x == 0)
    {
        cout << "Invalid Input. Please enter a number greater than 0" << endl;
        return false;
    }

    return true;
}

bool isInputNumber(const string& s)
{
    string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}

void printFactors(int number)
{
    int temp = 1;
    cout << "The factors of " << number << " are:" << endl;
    while (temp <= sqrt(number))
    {
        if (!(number % temp))
        {
            int x = number / temp;
            cout << temp << " * " << x << endl;
        }
        temp++;
    }
}

bool isPerfectNumber(int num)
{
    int i, div, sum = 0;
    for (i=1; i < num; i++)
    {
        div = num % i;

        if (div == 0)
        {
            sum = sum + i;
        }
    }

    if (sum == num)
    {
        return true;
    }
    return false;
}

int main()
{
    cout << "This program determines whether an integer is a perfect number" << endl;
    cout << endl;
    cout << "Enter a natural integer: ";

    string input;
    cin >> input;
    cout << endl;

    if(isInputNumber(input))
    {
        int x;
        stringstream strToNum(input);
        strToNum >> x;

        if(validateInputNumber(x))
        {
            if(isPerfectNumber(x))
            {
                cout << "The integer " << x << " is a perfect number" << endl;
                cout << endl;
            }
            else
            {
                cout << "The integer " << x << " is a not perfect number" << endl;
                cout << endl;
            }
            printFactors(x);
        }
    }
    else
    {
        cout << "Invalid Input. Please retry" << endl;
    }

    return 0;
}
