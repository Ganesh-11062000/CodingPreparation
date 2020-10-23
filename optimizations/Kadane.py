'''
//	Kadane's Algoritm -> Largest sum in Contiguous Array
	
//	function kadane_algo(arr):
//	1	max_current = arr[0]
//	2	max_global  = arr[0]
//	3	
//	4	for i = 1 upto i < n:
//	5		max_current = max(arr[i],max_current + arr[i])
//	6		if max_current > max_global:
//	7			max_global = max_current
//	8	
//	9	return max_global
		
		
#include<bits/stdc++.h>
using namespace std;

int kadane_algo(int arr[],int n){
	int max_current = arr[0];
	int max_global  = arr[0];
	int start = 0,end = 0;			//optional indices
	
	for(int i = 1;i < n;i++)
	{
		if (arr[i] < arr[i] + max_current)
		{
			max_current = max_current + arr[i];
			
		}else{
			max_current = arr[i];
			start = i;
			
		}
		
		if(max_current > max_global)
		{
			max_global = max_current;
			end = i;
		}
	}
	cout << "Start = " << start << ", End = " << end << endl;
	return max_global;
}


int main(){
	int n;
	cin >> n;
	
	int arr[n];
	for(int i = 0;i < n;i++){
		cin >> arr[i];
	}
	
	cout << "Largest Sum = " << kadane_algo(arr,n);
	
	return 0;
}

//	Output :
//	8
//	-2 -3 4 -1 -2 1 5 -3
//	Start = 2, End = 6
//	Largest Sum = 7

'''

def Kadane(arr):
	max_current = arr[0]
	max_global = arr[0]

	for i in range(1,len(arr)):
		max_current = max(arr[i],max_current+arr[i])

		if max_global < max_current:
			max_global = max_current

	return max_global 