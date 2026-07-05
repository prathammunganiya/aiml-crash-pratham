class Learner:

    def __init__(self, name, track):
        self.name = name
        self.track = track

    def summary(self):
        return f"{self.name} is learning {self.track}"

student = Learner("Pratham", "Artificial Intelligence")

print(student.summary())