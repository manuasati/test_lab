#include<iostream>
#include<stdlib.h>
#include<cmath> 
#include <string> 
#include <sstream> 

using namespace std;

double getDistance(double x1, double y1, double x2, double y2)
{
    // Calculating distance 
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) * 1.0);  
}

bool isNumber(string& s)
{
    std::stringstream sstr(s);
    float f;

    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return (!((sstr >> noskipws >> f).rdstate() ^ ios_base::eofbit) || (!s.empty() && it == s.end()));
}

int main()
{
    string inputNumber;
    int x1, y1, x2, y2;
    double distance;
    bool valid_number = false;
    cout << "This program calculates the distance between two points" << endl;

    cout << "Enter the coordinates of the first point" << endl;
    cout << "X: ";
    do{
        cin >> inputNumber;
        if (isNumber(inputNumber) == 0){
            cout << "Invalid Entry, enter valid entry!" << endl;
            cout << "X: ";
            continue;
        }
        stringstream strToNum(inputNumber);
        strToNum >> x1;      
        valid_number = true;
    }while(valid_number != true);
    valid_number = false;

    cout << "Y: ";
    do{
        cin >> inputNumber;
        if (isNumber(inputNumber) == 0){
            cout << "Invalid Entry, enter valid entry!" << endl;
            cout << "Y: ";
            continue;
        }
        stringstream strToNum(inputNumber);
        strToNum >> y1;      
        valid_number = true;
    }while(valid_number != true);
    valid_number = false;

    cout << endl;

    cout << "Enter the coordinates of the second point" << endl;
    cout << "X: ";
    do{
        cin >> inputNumber;
        if (isNumber(inputNumber) == 0){
            cout << "Invalid Entry, enter valid entry!" << endl;
            cout << "X: ";
            continue;
        }
        stringstream strToNum(inputNumber);
        strToNum >> x2;      
        valid_number = true;
    }while(valid_number != true);
    valid_number = false;

    cout << "Y: ";
    do{
        cin >> inputNumber;
        if (isNumber(inputNumber) == 0){
            cout << "Invalid Entry, enter valid entry!" << endl;
            cout << "Y: ";
            continue;
        }
        stringstream strToNum(inputNumber);
        strToNum >> y2;      
        valid_number = true;
    }while(valid_number != true);
    cout << endl;

    distance = getDistance(x1, y1, x2, y2);
    cout << "The distance between these two points is: " << distance;

    return 0; 
}
