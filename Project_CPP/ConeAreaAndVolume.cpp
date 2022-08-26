#include<iostream>
#include<stdlib.h>
#include<cmath> 
#include <string> 
#include <sstream> 

using namespace std;

bool isNumber(string& s)
{
    std::stringstream sstr(s);
    float f;

    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return (!((sstr >> noskipws >> f).rdstate() ^ ios_base::eofbit) || (!s.empty() && it == s.end()));
}

double getConeSurfaceArea(double radius, double height)
{
    double surfaceArea = -1;
    if(radius !=0 && height !=0)
    {
        surfaceArea = 3.14 * radius * (radius + sqrt(radius * radius + height * height));
    }
    
    return surfaceArea;
}

double getConeVolume(double radius, double height)
{
    double volume = -1;
    if(radius !=0 && height !=0)
    {
        volume = (1.0/3) * 3.14 * radius * radius * height;       
    }

    return volume;
}


int main()
{
    string inputNumber;
    double radius, height, surfaceArea, volume;
    bool valid_number = false;

    cout << "This program calculates the area and volume of a cone" << endl;
    cout << "Enter the radius of the cone: ";
    do{
        cin >> inputNumber;
        if (isNumber(inputNumber) == 0){
            cout << "Invalid Entry, enter valid entry!" << endl;
            cout << "Enter the radius of the cone: ";
            continue;
        }
        stringstream strToNum(inputNumber);
        strToNum >> radius;      
        valid_number = true;
    }while(valid_number != true);
    valid_number = false;

    cout << endl;

    cout << "Enter the height of the cone: ";
    do{
        cin >> inputNumber;
        if (isNumber(inputNumber) == 0){
            cout << "Invalid Entry, enter valid entry!" << endl;
            cout << "Enter the height of the cone: ";
            continue;
        }
        stringstream strToNum(inputNumber);
        strToNum >> height;      
        valid_number = true;
    }while(valid_number != true);

    cout << endl;

    surfaceArea = getConeSurfaceArea(radius, height);
    volume = getConeVolume(radius, height);

    cout << "The total area of the cone is: " << surfaceArea << endl;
    cout << "The volume of the cone is: " << volume << endl;

    return 0;
}
