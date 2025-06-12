def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
        else:
            next_multiple = ((grade + 4) // 5) * 5
            if next_multiple - grade < 3:
                new_grades.append(next_multiple)
            else:
                new_grades.append(grade)
    return new_grades