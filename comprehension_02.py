names = ["Jim", "Steve", "Kim", "Laura", "Phil", "Jon"]

filtered_list = [name for name in names if len(name) == 3]
# [value_to_include for original_value in original_list if some_condition_is_true]

# filtered_list = []
# for name in names:
#     if len(name) == 3:
#         filtered_list.append(name)

print(filtered_list)
