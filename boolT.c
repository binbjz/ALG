#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    long num;
    long sum = 0L;
    bool inputB;

    printf("Please enter an integer to be summed. ");
    printf("(q to quit): ");
    inputB = (scanf("%ld", &sum) == 1);

    while(inputB)
    {
        sum += num;
        printf("Please enter next integer (q to quit): ");
        inputB = (scanf("%ld", &sum) == 1);
    }
    printf("Those integers sum to %ld.\n", sum);
    return 0;
}
