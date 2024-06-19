from person import Student, Teacher, Doctor
from ward import Ward

if __name__ == "__main__":
    student1 = Student(name="studentA", yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1 . add_person(teacher1)
    ward1 . add_person(teacher2)
    ward1 . add_person(doctor1)
    ward1 . add_person(doctor2)
    ward1 . describe()
    print(f"Number of doctors: {ward1.count_doctor()}")
    print("After sorting Age of Ward1 people")
    ward1.sort_age()
    ward1.describe()
    print(f"Average year of birth (teachers): {ward1.compute_average()}")
