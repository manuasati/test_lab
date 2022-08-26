#include<iostream>
#include<stdlib.h>
#include<time.h>
#include <string>
#include <sstream>

using namespace std;

bool isNumber(const string& s)
{
    string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}

bool checkInput(string& strGuessedNumber)
{
    getline (cin, strGuessedNumber);
    if (isNumber(strGuessedNumber) == 0){
        cout << "Invalid entry!" << endl;
        return false;
    }

    return true;
}

int generateRandNo()
{
    int generatedNo;
    generatedNo = rand()%100 + 1;
    return generatedNo;
}

bool matchGuessNoWithRandomNumber(int generatedNumber)
{
    string strGuessedNumber;
    int guessedNumber, noOfTries;
    noOfTries = 0;

    if(!checkInput(strGuessedNumber))
    {
        return false;
    }

    stringstream strToNum(strGuessedNumber);
    strToNum >> guessedNumber;

    if (guessedNumber < generatedNumber)
    {
        cout << "Too low, the number I have chosen is greater than " << guessedNumber << endl;
        return false;
    }
    else if(guessedNumber > generatedNumber)
    {
        cout << "Too high, the number I chose is smaller than " << guessedNumber << endl;
        return false;
    }

    return true;
}


int main()
{
    // This program will create different sequence of
    // random numbers on every program run

    // Use current time as seed for random generator
    srand(time(0));

    cout << "Game-Guess my number Version 1.0" << endl;
    cout << "==================================" << endl;

    cout << "I chose a number between 1 and 100" << endl;
    cout << "Can you guess that number: ";

    int noOfTries;
    int generatedNumber = generateRandNo();;
    noOfTries = 0;

    while(!matchGuessNoWithRandomNumber(generatedNumber))
    {
        noOfTries++;
        cout << "To try a NEW: ";
    }

    cout << "==================================" << endl;
    cout << "Bravo! You have Guess The number after " << noOfTries << " tries" << endl;

    return 0;
}
