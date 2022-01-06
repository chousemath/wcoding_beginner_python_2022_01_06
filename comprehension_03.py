grades = [100, 89, 76, 45]

threshold = 80

students_who_need_help = [grade for grade in grades if grade < threshold]

print(students_who_need_help)
