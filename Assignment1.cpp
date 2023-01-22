#include<iostream>
#include<array>
using namespace std;

int main(){
	int arraysize;
	int numbers[105];
	int target_no;
	int x=0;
	int y=0;
	int z;
	cout<<"Enter the number of elements of array";
	cin>>arraysize;
	cout<<"Enter the elements of array";
	while(x<arraysize){
		cin>>numbers[x];
		x++;
	}
	cout<<"Enter the target number";
	cin>>target_no;
	while(y<(arraysize-1)){
		z=y+1;
		while(z<arraysize){
			if((numbers[y]+numbers[z])==target_no){
				cout<<y;
				cout<<z;
		}
		z++;
	}
	y++;
}
}



