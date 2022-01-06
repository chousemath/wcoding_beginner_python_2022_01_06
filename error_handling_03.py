# ask the user for two numbers
# store those numbers in separate variables
# add those two numbers together and print out the result
# if an error occurs, don't crash, just ask the user again
# for two valid numbers
while True:
    try:
        num1 = int(input("Please input a number "))
        num2 = int(input("Please input another number "))
        result = num1 + num2
        break
    except Exception as e:
        print("Please input a valid number")
print(f"The sum of both numbers is {result}")
