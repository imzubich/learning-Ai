#1 method

num = int(input("Enter a number: "))  
factorial = 1  

for i in range(1, num + 1):  
    factorial *= i  

print("Factorial of " + str(num) + " is " + str(factorial))  
