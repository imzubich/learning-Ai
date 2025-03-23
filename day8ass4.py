numbers = [] 

for i in range(101):
    numbers.append(i)

num = int(input("Enter a number: "))
numbers.append(num) 

# print("List:", numbers) 


countnum3 = 0 

for num in numbers:  
    if '3' in str(num):
        countnum3 += 1  

print("Number 3 appears", countnum3, "times in the list.")
