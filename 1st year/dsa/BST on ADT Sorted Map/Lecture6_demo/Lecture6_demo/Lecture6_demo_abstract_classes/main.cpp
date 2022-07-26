#include "Penguin.h"
#include "Dog.h"
#include <Windows.h>
#include <iostream>
#include <vector>
#include "Zoo.h"
#include "Animal.h"

using namespace std;

int main()
{   Penguin p1{"black and white" , 7 , "Magellanic" } ;
    Animal* a2 = &p1 ;
    Animal* a3 = new Penguin{"black", 20, "pula"};
    a3->speak();
    ((Animal*)a3)->speak();
	return 0;
}