# def card_hide(card_number):
#     last_four = card_number[-4:]
#     prefix = "*" * (len(card_number) - 4)
#     return prefix + last_four


# def card_hide(card_number):
#     hidden_number = ""
#     for index, char in enumerate(card_number):
#         if index < len(card_number) - 4:
#             hidden_number += "*"
#         else:
#             hidden_number += char
#     return hidden_number
#

# print(card_hide("1234123456785678"))  # ➞ "************5678"
# print(card_hide("8754456321113213"))  # ➞ "************3213"
# print(card_hide("35123413355523"))  # ➞ "**********5523"

grads = ["Tom", "Jim", "Jane"]

# for index, grad in enumerate(grads):
#     print(f"{index}. {grad} graduated")

for index in range(len(grads)):
    grad = grads[index]
    print(f"{index}. {grad} graduated")
