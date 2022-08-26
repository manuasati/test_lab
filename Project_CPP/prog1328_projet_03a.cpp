/*****************************************************************************
Description:		Ce programme porte sur la manipulation de chaînes de
caractères.
Fichier source:		prog1328_projet_03a.cpp
Programmeur:
******************************************************************************/

#include <iostream>
#include <cctype>   

/*****************************************************************************/
/* prototypes de fonctions */

void upperCase(char* s);

void titleCase(char* s);

/*****************************************************************************/
int main()
{
	char str[256] = "";

	// Pilote pour la fonction upperCase()
	std::cout << "=================================================================\n\n";
	std::cout << "La fonction upperCase() permet de mettre une chaine en majuscule\n\n";

	std::cout << "Entrez une chaine: ";
	std::cin.getline(str, 256);

	std::cout << "\nLa chaine AVANT l'appel de upperCase() est: " << str << "\n\n";

	upperCase(str);

	std::cout << "La chaine APRES l'appel de upperCase() est: " << str << "\n\n";


	// Pilote pour la fonction titleCase()
	std::cout << "=================================================================\n\n";

	memset(str, '\0', 256); //remplie chaque cellule de la chaine avec le caractere nul.

	std::cout << "La fonction titleCase() permet de mettre une chaine en format titre\n\n";

	std::cout << "Entrez une chaine: ";
	std::cin.getline(str, 256);

	std::cout << "\nLa chaine AVANT l'appel de titleCase() est: " << str << "\n\n";

	titleCase(str);

	std::cout << "La chaine APRES l'appel de titleCase() est: " << str << "\n\n\n";

	return 0;
}

/*****************************************************************************/

void upperCase(char* s)
{


}

/*****************************************************************************/

void titleCase(char* s)
{


}