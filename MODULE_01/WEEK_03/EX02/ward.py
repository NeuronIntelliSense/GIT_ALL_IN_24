class Ward():
    def __init__(self, name):
        self.name = name
        self.list_person = []

    def add_person(self, person):
        self.list_person.append(person)

    def describe(self):
        print(f"Ward name: {self.name}")
        for person in self.list_person:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.list_person:
            if person.job == "doctor":
                count += 1
        return count

    def compute_average(self):
        total = 0
        count = 0
        for person in self.list_person:
            if person.job == "teacher":
                total += person.yob
                count += 1
        return total/count

    def sort_age(self):
        self.list_person.sort(key=lambda x: x.yob, reverse=True)
