#include<iostream>
#include<stdlib.h>
#include<cmath>
#include<sstream>
#include<vector>

using namespace std;

bool validateInputNo(int x)
{
    if(x < 0 || x == 0)
    {
        cout << "Invalid Input. Please enter a number greater than 0" << endl;
        return false;
    }

    if(x == 1)
    {
        cout << "1 is neither prime nor composite" << endl;
        return false;
    }

    return true;
}

bool isNumber(const string& s)
{
    string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}

bool isPrimeNum(int n)
{
    bool isPrime = true;

    for(int i = 2; i <= n / 2; ++i)
    {
      if(n % i == 0)
      {
          isPrime = false;
          break;
      }
    }

    return isPrime;
}


void printPrime(int n)
{
    bool result = false;
    vector<int> resVec;

    for(int i=2; i<=n; i++)
    {
        result = isPrimeNum(i);
        if(result)
        {
            resVec.push_back(i);
        }
    }

    cout << "The prime numbers from 2 to " << n << " are:" << endl;
    vector<int>::iterator it;
    for(it = resVec.begin(); it != resVec.end(); it++)
    {
        cout << *it << endl;
    }
}

int main()
{
    cout << "This program determines whether an integer is a prime number" << endl;
    cout << "====================================" << endl;

    string input;

    while(true)
    {
        cout << "Enter a choice of operation" << endl;
        cout << endl;
        cout << "d To determine if a number is prime" << endl;
        cout << "a To display all the prime numbers until a number given" << endl;
        cout << "q To exit the program" << endl;

        cin >> input;

        string inputNo;
        if(input == "d" || input == "D")
        {
            cout << "Enter a natural integer: ";
            cin >> inputNo;

            if(isNumber(inputNo))
            {
                int x;
                stringstream strToNum(inputNo);
                strToNum >> x;
                if(validateInputNo(x))
                {
                    if(isPrimeNum(x))
                    {
                        cout << "The integer " << x << " is a prime number" << endl;
                    }
                    else
                    {
                        cout << "The integer " << x << " is not a prime number" << endl;
                    }
                }
            }
            else
            {
                cout << "Please provide a valid input No" << endl;
            }
        }
        else if(input == "A" || input == "a")
        {
            cout << "Enter the number until Which you want to display the prime numbers: ";
            cin >> inputNo;

            if(isNumber(inputNo))
            {
                int x;
                stringstream strToNum(inputNo);
                strToNum >> x;
                if(validateInputNo(x))
                {
                    printPrime(x);
                }
            }
            else
            {
                cout << "Please provide a valid input No" << endl;
            }
        }
        else if(input == "Q" || input == "q")
        {
            break;
        }
        else
        {
            cout << "Invalid Input. Please try again." << endl;
        }
    }

    return 0;
}
