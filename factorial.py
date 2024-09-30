...
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes

...

n = int(input())
if n < 1:
    print("No")  # Factorials are defined for positive integers only
else:
    factorial_value = 1
    i = 1
    while factorial_value < n:
        i += 1
        factorial_value *= i
    if factorial_value == n:
        print("Yes")
    else:
        print("No")

