ages = [100, 55, 76, 23, 19]

# create a list comprehension which
# selects only the even ages from the original list
# and prints those values out

filtered_ages = [age for age in ages if age % 2 == 0]

# filtered_ages = []

# for age in ages:
#     if age % 2 == 0:
#         filtered_ages.append(age)

print(filtered_ages)
