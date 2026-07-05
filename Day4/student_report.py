# Student Report System using OOP

class Student:
    school_name = "AIML Academy"

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (
            f"School: {Student.school_name} | "
            f"Name: {self.name} | "
            f"Roll No: {self.roll_no} | "
            f"Average: {self.average():.2f} | "
            f"Grade: {self.grade()}"
        )


student1 = Student("Pratham", 101, [95, 88, 92])
student2 = Student("Rahul", 102, [78, 82, 80])
student3 = Student("Aman", 103, [65, 70, 68])

print(student1)
print(student2)
print(student3)