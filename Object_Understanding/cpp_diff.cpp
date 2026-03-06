#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	cout<<"String implementation and diff\n";
	string strr = "Akshaya Baalaji S";
	cout<<"Size = " << strr.size() <<endl;
	// cout<<"Size = " << ("Akshaya Baalaji").size() <<endl;
	// this is the proof that the python treat the value as obj and the cpp treat the value as raw value in memory 

	std::vector vectt = {12,23,34,45,45};
	cout<<"Vectt size  =  " << vectt.size() <<endl;
	cout<<"Vectt size  =  " << ({12,23,34,45,45}).size() <<endl;
}