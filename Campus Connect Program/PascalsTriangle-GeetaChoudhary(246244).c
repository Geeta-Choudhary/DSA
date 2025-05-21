/*Pascals triangle code without the nCr formula*/

#include <stdio.h>

int main()
{
    int rows, i, j, space, value;

    // Ask the user to enter the number of rows for Pascal's Triangle
    printf("Enter the number of rows for Pascal's Triangle: ");
    scanf("%d", &rows);

    // Generate Pascal's Triangle
    for (i = 1; i <= rows; i++)
    {
        // Print leading spaces for alignment
        for (space = 1; space <= (rows - i); space++)
        {
            printf(" ");
        }

        // Calculate and print each value in the row
        for (j = 1; j <= i; j++)
        {
            if (i == 1 || j == 1)
            {
                value = 1;
            }
            else
            {

                value = value * (i - j + 1) / (j-1); // Update the value based on the binomial coefficient formula
            }
            printf("%2d ", value);
        }
        printf("\n"); // Move to the next row
    }

    return 0;
}
