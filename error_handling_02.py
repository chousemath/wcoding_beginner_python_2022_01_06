while True:
    try:
        salary = input("Please input your current salary: ")
        salary = int(salary)
        salary *= 100
        break
    except Exception as e:
        print("Please input a valid salary number")

print(f"Your new salary is ${salary}")
