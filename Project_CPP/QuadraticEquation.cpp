#include<iostream>
#include<stdlib.h>
#include<cmath>
#include<sstream>

using namespace std;

bool isNumber(string& s)
{
    std::stringstream sstr(s);
    float f;

    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return (!((sstr >> noskipws >> f).rdstate() ^ ios_base::eofbit) || (!s.empty() && it == s.end()));
}

bool validateInput(string& inputNumber, string& inputMsg)
{
    bool validNumber = false;
    do{
        cin >> inputNumber;
        if(isNumber(inputNumber) == 0){
            cout << "Invalid Entry, enter valid entry!" << endl;
            cout << inputMsg;
            continue;
        }
        validNumber = true;
    }while(validNumber != true);
    return validNumber;
}

void assignInput(float& x, string& input)
{
    stringstream strToNum(input);
    strToNum >> x;
}

float getDiscriminant(float a, float b, float c)
{
    return b*b - 4*a*c;
}

float getQuadraticRootX1(double a, double b, double sqrt_val)
{
    return ((double)(-b + sqrt_val)/(2*a));
}

float getQuadraticRootX2(double a, double b, double sqrt_val)
{
    return ((double)(-b - sqrt_val)/(2*a));
}

void findRoots(float a, float b, float c)
{
    // If a is 0, then equation is not quadratic, but
    // linear
    if (a == 0)
    {
        cout << "Invalid";
        return;
    }

    float d = getDiscriminant(a, b, c);
    double sqrt_val = sqrt(abs(d));

    if (d > 0)
    {
        cout << "This program is used to calculate the roots of the quadratic equation: Ax ^ 2 + bx + c = 0" << endl;
        cout << "The root X1 = " << getQuadraticRootX1(a, b, sqrt_val) << endl
            << "The root X2 = " << getQuadraticRootX1(a, b, sqrt_val) << endl;
    }
    else if (d == 0)
    {
        cout << "This program is used to calculate the roots of the quadratic equation: ax2 bx CE" << endl;
        cout << "The Discriminant, B2-4ac, is E, then there is only one root" << endl;
        cout << "The root x1 = " << -(double)b / (2*a);
    }
    else // d < 0
    {
        cout << "This program is used to calculate the roots of the quadratic equation: axA2 bxc0" << endl;
        cout << "The discriminant, b ^2 – 4AC, is inferior to 0, then the roots are imaginary" << endl;
        cout << "The root x1 = " << -(double)b / (2*a) << " + i" << sqrt_val
            << endl << "The root x2 = " << -(double)b / (2*a) << " - i"
            << sqrt_val << endl;
    }
}

// Driver code
int main()
{
    float a, b, c;
    string inputNumber;

    string inputMsg = "Enter the value of ' a ': ";
    cout << inputMsg ;
    if(validateInput(inputNumber, inputMsg))
    {
        assignInput(a, inputNumber);
    }
    cout << endl;

    inputMsg = "Enter the value of ' b ': ";
    cout << inputMsg ;
    if(validateInput(inputNumber, inputMsg))
    {
        assignInput(b, inputNumber);
    }
    cout << endl;

    inputMsg = "Enter the value of ' c ': ";
    cout << inputMsg ;
    if(validateInput(inputNumber, inputMsg))
    {
        assignInput(c, inputNumber);
    }
    cout << endl;

    findRoots(a, b, c);
    return 0;
}
