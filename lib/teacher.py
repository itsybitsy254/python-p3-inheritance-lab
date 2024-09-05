# teacher.py

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "Python programming",
            "Data structures",
            "Algorithms",
            "Machine learning",
            "Artificial intelligence",
            "Computer networks",
            "Cybersecurity",
            "Database management"
        ]

    def teach(self):
        return random.choice(self.knowledge)
