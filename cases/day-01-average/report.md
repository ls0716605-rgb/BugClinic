
# Case 001: Average Calculator

## 1. Problem
What is the programme supposed to do?

## 2. Actual behaviour
What happened when the code ran?

## 3. Error evidence
What did Python report?

## 4. Root cause
Why did the error occur?

## 5. Correction
What did you change and why?

## 6. Testing
Which inputs did you test?

## 7. Final result
Did all expected behaviours pass?

# Case 001: Student Average Calculator

**Project:** BugClinic – AI Code Debugging & Quality Assurance Laboratory  
**Case Number:** 001  
**Date:** 24 November 2026  
**Programming Language:** Python  
**Bug Category:** Runtime Error – ZeroDivisionError  
**Status:** Resolved

---

## 1. Problem Description

An AI-generated Python programme was designed to calculate the average marks of students.

The programme worked correctly when provided with a list containing marks. However, it crashed when an empty list was provided.

The expected behaviour was:
- Calculate the average for a non-empty list.
- Return `None` when the list is empty.
- Reject marks outside the permitted range of 0–100.

## 2. Original Code

The original programme was:

```python
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


student_marks = [70, 80, 90]

print(calculate_average(student_marks))
print(calculate_average([]))
```

## 3. Actual Behaviour

When the programme received `[70, 80, 90]`, it returned `80.0`.

However, when it received an empty list, Python raised a `ZeroDivisionError`.

### Error details

The error occurred because the programme attempted to divide the total by the number of elements in an empty list.

## 4. Root Cause Analysis

The problematic statement was:

```python
average = total / len(marks)
```

For an empty list:

- `sum([])` returns `0`.
- `len([])` returns `0`.
- The programme attempts to calculate `0 / 0`.

Python does not allow division by zero, resulting in a `ZeroDivisionError`.

**Root cause:** The original function did not validate whether the list contained elements before performing division.

## 5. Implemented Solution

I introduced input validation before performing the average calculation.

The improved programme:
- Returns `None` for an empty list.
- Rejects marks below 0 or above 100 using `ValueError`.
- Calculates the average for valid marks.

### Corrected Code

```python
def calculate_average(marks):

    if len(marks) == 0:
        return None

    for num in marks:
        if num < 0 or num > 100:
            raise ValueError(
                "Marks must be between 0 and 100"
            )

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
```

## 6. Testing and Verification

The corrected programme was tested using different inputs.

| Test input | Expected result | Status |
|---|---|---|
| `[70, 80, 90]` | 80.0 | PASS |
| `[50]` | 50.0 | PASS |
| `[]` | None | PASS |
| `[-20, 80, 90]` | ValueError | PASS |
| `[100, 110, 90]` | ValueError | PASS |

All expected behaviours were achieved.

## 7. Final Result

The original runtime error was successfully resolved.

The improved function now handles empty lists and validates mark ranges before calculating an average.

The correction also makes the function more reliable when receiving different inputs.

## 8. Lessons Learned

Through this debugging exercise, I learned:

1. How to identify a ZeroDivisionError using a Python traceback.
2. How to investigate the root cause of a runtime error.
3. How to use conditional statements for input validation.
4. How to distinguish between returning None and raising an exception.
5. Why testing different inputs is important when fixing software defects.

---

**Case Status:** RESOLVED  
**Project:** BugClinic  
**Author:** Team BugClinic