#include <stdio.h>

int main()
{
    // Declare variables for storing the number and an array of to hold binary digits
    int number, arr[32], index = 0;

    // Ask the user to enter a number
    printf("Enter the number:");
    scanf("%d", &number);

    // Handle the  case where the number is zero
    if (number == 0)
    {
        printf("Binary representation: 0\n");
        return 0;
    }

    // Convert the number to binary by repeatedly dividing by 2
    while (number > 0)
    {
        arr[index++] = number % 2; // Store the remainder (binary digit) in the array
        number = number / 2;       // Update the number by dividing it by 2
    }

    // Print the binary representation in reverse order
    printf("Binary representation: ");
    for (int i = index - 1; i >= 0; i--)
    {
        printf("%d", arr[i]); // Print the binary digits in reverse order
    }
    printf("\n");

    return 0;
}
