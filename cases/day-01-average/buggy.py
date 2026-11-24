
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


student_marks = [70, 80, 90]

print(calculate_average(student_marks))
print(calculate_average([]))
