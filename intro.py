name = "Pratham"
city = "Banswara"
favorite_subject = "OOPs"
target_role = "Software Engineer"

student = {
    "name": name,
    "city": city,
    "favorite_subject": favorite_subject,
    "target_role": target_role
}

print(f"My name is {student['name'].title()}.")
print(f"I live in {student['city'].upper()}.")
print(f"My favorite subject is {student['favorite_subject']}.")
print(f"My target role is {student['target_role']}.")