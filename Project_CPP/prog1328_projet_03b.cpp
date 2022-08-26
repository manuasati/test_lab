/*****************************************************************************
Description:		Ce programme porte sur la manipulation de chaînes de
caractères.
Fichier source:		prog1328_projet_03b.cpp
Programmeur:
******************************************************************************/

#include <iostream>		

#define STRSIZE 100

/*****************************************************************************/
/* prototypes de fonctions */

bool getCommaPosition(const char* fullName, int* commaPos);
void getLastName(const char* fullName, char* lastName);
void getFirstName(const char* fullName, char* firstName);

/*****************************************************************************/
int main()
{
	char fullName[STRSIZE] = "";
	char lastName[STRSIZE] = "";
	char firstName[STRSIZE] = "";

	int commaPosition = 0;

	std::cout << "SVP entrez un nom dans le format \"Nom,Prenom\": ";

	std::cin.getline(fullName, STRSIZE);

	if ((getCommaPosition(fullName, &commaPosition) == true) && (commaPosition != 0))
	{
		std::cout << std::endl << std::endl << std::endl;
		std::cout << "La position de la virgule dans la chaine est: " << commaPosition << std::endl;

		getLastName(fullName, lastName);
		std::cout << std::endl << std::endl;
		std::cout << "Le nom est: " << lastName << std::endl;

		getFirstName(fullName, firstName);
		std::cout << std::endl << std::endl;
		std::cout << "Le prenom est:" << firstName << std::endl;
	}
	else
	{
		std::cout << std::endl << std::endl;
		std::cout << "Le nom \"" << fullName << "\" n'est pas valide." << std::endl << std::endl;
	}

	return 0;
}


/*****************************************************************************/
/* La fonction trouve la position de la virgule pour un nom
dans le format "Nom,Prenom". */

bool getCommaPosition(const char* fullName, int* commaPos)
{
	int i = 0;

	while (fullName[i] != '\0')
	{
		if (fullName[i] == ',')
		{
			*commaPos = i;
			return true;
		}
		i++;
	}
	return false;
}

/*****************************************************************************/

void getLastName(const char* fullName, char* lastName)
{


}

/*****************************************************************************/

void getFirstName(const char* fullName, char* firstName)
{


}