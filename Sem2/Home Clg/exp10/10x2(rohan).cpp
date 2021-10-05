// EXPERIMENT – 10

// Title: Hash tables
// Objective: To understand the concepts of Hash tables

// 2. Implement a Hash table using arrays. Perform Insert, Delete and Search operations on the hash
// table using the above Hash function. Adopt a suitable user-defined exception handling strategy
// if collision occurs while inserting data.

#include<iostream>
#include<exception>
using namespace std;

#define FAMILY_LENGTH 10

class CollisionException: public exception{

	public:
		const char * what() const throw(){
			return "Collision Occured!\n";
		}

};

class HashTable{

	unsigned long table[FAMILY_LENGTH];

public:
	HashTable(){
		for(int i{}; i<FAMILY_LENGTH; i++) table[i]= 0;
	}

	long get_hash(unsigned long sap) const {
		unsigned long sum{sap%1000};
		while(sum>9) sum-=9;
		return sum;
	}

	long search(unsigned long sap) const {
		long i= get_hash(sap);
		if(table[i]==sap) return i;
		else return -1;
	}

	void insert(unsigned long sap){
		long i= get_hash(sap);
		if(table[i]==0){
			table[i]= sap;
			cout<<("SAP:%lu added!\n", sap);
		}else if(table[i]!=sap) throw CollisionException{};
	}

	void del(unsigned long sap){
		long pos= search(sap);
		if(pos!=-1){
			table[pos]= 0;
			cout<<("SAP: %lu deleted.\n", sap);
		}else{
			cout<<("SAP:%lu not found!\n", sap);
		}
	}

};

int main(){
    HashTable db;

	short ans{};
	unsigned long sap{};
	while(1){
		cout<<("\nChoose one of the following options.\n");
		cout<<("1. Insert new SAP\n2. Delete SAP\n3. Search SAP\n4. Exit.\n");
		cout<<("Enter>>");
		cin>>ans;
		switch(ans){
			case 1:
			    {
				cout<<("Enter new SAP:");
				cin>>sap;
				try{
					db.insert(sap);
				}catch(const CollisionException& e){
					cout<<("Exception Occured! %s\n", e.what());
				}
			}
			break;
			case 2:
			    {
				cout<<("Enter SAP to be deleted:");
				cin>>sap;
				db.del(sap);
			}
			break;
			case 3:
			    {
				cout<<("Enter SAP to be searched:");
				cin>>sap;
				long pos= db.search(sap);
				if(pos==-1) cout<<("SAP %lu not found!\n", sap);
				else cout<<("SAP %lu found at %lu.\n", sap, pos);
			}
			 break;
			case 4:
			    {
				return 0;
			}
			break;
			default:
			    {
				cout<<("Incorrect Choice!\n");
			}
		}
	}

}
