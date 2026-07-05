# Student CSV Records

import csv


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    return "F"


with open("Day4/students.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("Day4/results.csv", "w", newline="") as output:
        fields = ["name", "average", "grade"]
        writer = csv.DictWriter(output, fieldnames=fields)

        writer.writeheader()

        for row in reader:
            avg = (
                int(row["math"]) +
                int(row["science"]) +
                int(row["english"])
            ) / 3

            writer.writerow({
                "name": row["name"],
                "average": round(avg, 2),
                "grade": grade(avg)
            })