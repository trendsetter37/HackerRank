#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void read_array(int length, int *arr) // Reads in array input
{
    int i = 0;
    while(i < length && scanf("%d", &arr[i++]) == 1);
}

long int coin_change(const int N, int *coins, int length)
{
    int i;
    int j;
    int size = N + 1;
    long res[size];
    memset(res, 0, sizeof res);
    res[0] = 1;
    for (i = 0; i < length; i++){
        for(j = coins[i]; j < size; j++) {
            res[j] += res[j - coins[i]];
        }
    }
    return res[N];
}

int main() {

    int N;
    int M;
    int input[50] = {0};
    scanf("%d %d", &N, &M);
    read_array(M, input);
    printf("%ld", coin_change(N, input, M));
    return 0;
}
