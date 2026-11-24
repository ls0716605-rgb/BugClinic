
def calculate_average(marks):

    if len(marks) == 0:
        return None

    for num in marks:
        if num < 0 or num > 100:
            raise ValueError("Marks must be between 0 and 100")

    total = sum(marks)
    average = total / len(marks)

    return average


print(calculate_average([70, 80, 90]))
print(calculate_average([50]))
print(calculate_average([]))

try:
    print(calculate_average([-20, 80, 90]))
except ValueError as error:
    print("Invalid input:", error)
