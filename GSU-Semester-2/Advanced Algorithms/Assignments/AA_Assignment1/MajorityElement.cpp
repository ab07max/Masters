/* C++ Program for finding out majority (strictly more than n/2) element in an array */


/*
The idea behind implementation:
1. take the user input in the array
2. find the frequently occured element
3. check if the frequently occured element is frequented more than n/2 times where n is size of array
4. print the frequented element
*/


#include <iostream> 
using namespace std;

/* Function to check if the most frequent element occurs more than n/2 times */
bool isMaxFrequent(int a[], int size, int freq) {
	int count = 0;
	for (int i = 0; i < size; i++)
		if (a[i] == freq)
			count++;
	if (count > (size / 2))
		return 1;
	else
		return 0;
}

/* Function to find the most frequent element */
int frequentElement(int a[], int size) {
	int freq_index = 0, count = 1;
	for (int i = 1; i < size; i++) {
		// if the same element is found in the subsequent itertion increase the count
		if (a[freq_index] == a[i])
			count++;
		// if the same variable is not found decrease the count of the frequency
		else
			count--;
		// once the count becomes zero we start out with a new element in the array as the frequent element 
		if (count == 0) {
			freq_index = i;
			count = 1;
		}
	}
	return a[freq_index];
}

/* Function to print frequently occured element */
void printMajority(int a[], int size) {
	/* Find the frequently occured element*/
	int freq_element = frequentElement(a, size);

	/* Print the candidate if it is Majority*/
	if (isMaxFrequent(a, size, freq_element))
		std::cout << "Frequent Element: " << freq_element << " ";
	else
		std::cout << "No Majority Element found!";
}

/* Driver Code */
int main() {
	int n; //variable to hold the size of the array
	std::cout << "How many elements in the array? "<< endl;
	std::cin >> n;
	int* a; //dynamic allocation of array size and elements
	a = new int[n];
	std::cout << "Input the elements in the array: " << endl;
	
	for (int i = 0; i < n; i++)
		std::cin >> a[i];
	
	// Function calling 
	printMajority(a, n);

	return 0;
}

/*
	Other information:
	Time Complexity: O(n) - as all the comparisions happen within a loop variant
	Space Complexity: O(1) - as there is no external space used except for the array itself
*/