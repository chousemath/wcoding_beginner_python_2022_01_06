# + - / *


def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        if num2 == 0:
            return "Can't divide by 0!"
        return num1 / num2
    elif operator == "*":
        return num1 * num2
    else:
        return f"Cannot handle operator: {operator}"


print(calculator(2, "+", 2))  # ➞ 4
print(calculator(2, "*", 2))  # ➞ 4
print(calculator(2, "*", 5))  # ➞ 10
print(calculator(4, "/", 2))  # ➞ 2
print(calculator(4, "/", 0))  # ➞ ??
print(calculator(4, "?", 3))  # ➞
