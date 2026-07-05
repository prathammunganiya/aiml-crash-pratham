# Student Profile Card using F-Strings and Type Hints

student = {
    "name": "Pratham",
    "course": "AIML",
    "city": "Banswara",
    "skills": ["Python", "Git", "Pandas"]
}

def profile_card(data: dict) -> str:
    return (
        f"Name   : {data['name']}\n"
        f"Course : {data['course']}\n"
        f"City   : {data['city']}\n"
        f"Skills : {', '.join(data['skills'])}"
    )

print(profile_card(student))