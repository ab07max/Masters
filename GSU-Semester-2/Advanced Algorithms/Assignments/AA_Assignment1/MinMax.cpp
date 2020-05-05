/* C++ implementation of Min and Max of an array of numbers in omega(1.5n - 2) comparisons */

/*
    Implementation Strategy:
    1. Accept the user input
    2. if the array size is just 1, min and max are that element
    3. if the array size is 2, then we just need one comparison for deciding min and max
    4. Used Divide and conquer strategy (Tournament method)
        a. find min and max for the smaller sublists
        b. combine those lists to find the min and max for larger lists.
*/

#include<iostream>
using namespace std;

struct minMaxPair {
    int min;
    int max;
};

struct minMaxPair getMinMax(int arr[], int low, int high) {
    struct minMaxPair minmax, mml, mmr;
    int mid;

    /* If there is only one element then that element becomes min and max*/
    if (low == high) {
        minmax.max = arr[low];
        minmax.min = arr[low];
        return minmax;
    }

    /* If there are two elements then it requies only one comparison to decide min and max*/
    if (high == low + 1) {
        if (arr[low] > arr[high]) {
            minmax.max = arr[low];
            minmax.min = arr[high];
        }
        else {
            minmax.max = arr[high];
            minmax.min = arr[low];
        }
        return minmax;
    }

    /* If there are more than 2 elements then we follow divide and conquer strategy */
    mid = (low + high) / 2;
    mml = getMinMax(arr, low, mid);
    mmr = getMinMax(arr, mid + 1, high);

    /* compare minimums of two parts */
    if (mml.min < mmr.min)
        minmax.min = mml.min;
    else
        minmax.min = mmr.min;

    /* compare maximums of two parts */
    if (mml.max > mmr.max)
        minmax.max = mml.max;
    else
        minmax.max = mmr.max;

    return minmax;
}

/* Driver code */
int main() {
    int arr_size;
    cout << "How many elements in the array?" << endl;
    cin >> arr_size;
    
    int* arr;
    arr = new int[arr_size];
    
    cout << "Enter elements of the array: " << endl;
    for (int i = 0; i < arr_size; i++)
        cin >> arr[i];

    struct minMaxPair minmax = getMinMax(arr, 0, arr_size - 1);
    cout << "Minimum Element: " + minmax.min << endl;
    cout << "Maximum Element: " + minmax.max << endl;
}

/*
    Other information:
    1. The recurrence relation for the above function is given as T(n) = 2 * T(n/2) + 2
        a. It is T(n/2) to compute the min and max of the halved pair
        b. we added 2 in the end, one to find mins between halves and other to find maxs between halves
    2. T(n) = 2 * (2 * T(n/2^2) + 2) + 2 => 2^2 * T(n/2^2) + 2^2 + 2
    3. T(n) = 2^k * T(n/2^k) + 2 + 2^2 + .... + 2^k
    4. T(n) = 2^(k+1)/2 * T(2^(k+1)/2^k) + 2(2^k - 1)   if n = 2^(k+1)
    5. T(n) = n/2 + 2(n/2 - 1)
    6. T(n) = 3n/2 -2

    Time Complexity: O(n)
*/