class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
        self.job = None


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
        self.job = "student"

    def describe(self):
        print(
            f"Student - Name: {self.name} - YOB: {self.yob} - Grade: {self.grade}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
        self.job = "doctor"

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YOB: {self.yob} - Specialist: {self.specialist}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
        self.job = "teacher"

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YOB: {self.yob} - Subject: {self.subject}")
