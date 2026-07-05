students = [
    {"name": "Pratham", "score": 92},
    {"name": "Pradume", "score": 81},
    {"name": "Purvam", "score": 74},
    {"name": "Pari", "score": 63},
    {"name": "Nandini", "score": 45}
]

def classify(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

students = sorted(students, key=lambda student: student["score"], reverse=True)

for student in students:
    grade = classify(student["score"])
    print(f"{student['name']} - Score: {student['score']} - Grade: {grade}")