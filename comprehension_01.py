salaries = [1_000, 5_300, 22_000]

# for index, salary in enumerate(salaries):
#     salaries[index] = salary + 500

# salaries = [salary - 1000 for salary in salaries]
# print(salaries)

names = ["Kim", "Jim", "Lim"]
# greetings = [f"Hey there {name}" for name in names]
greetings = []
for name in names:
    greetings.append(f"Hey there {name}")

print(greetings)
print(names)
