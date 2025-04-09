#IF ELIF AND ELSE
if 5 > 2:
    print("5 is greater than 2!")

#VARIABLES WITH MULTIPLE VALUES!
list = Name1, Name2, Name3, Name4, Name5 = "JOHN", "ALEXA", "STEVEN", "DOE", "BEN"

print(list)

print('Enter your first number: ')
num1 = input()
print('Enter your second number: ')
num2 = input()

print('First number before swapping: ' +num1)  
print('Second number before swapping: ' +num2)  

temp = num1
num1 = num2
num2 = temp

print('First number after swapping: ' +num1)
print('Second number after swapping: ' +num2)

print("Number 1 is" +temp)
