class Gradebook:
    def __init__(self):
        self.gradebook = []

    def add_student(self,name):
        grades = [name, []]
        self.gradebook.append(grades)


    def record_grade(self, name, subject, record):
        student_exist = False
        for student in self.gradebook:
            if student[0] == name:  # Check if the student exists
                student_exist = True
                for sub in student[1]:
                    if sub[0] == subject:  # If subject exists, append the grade
                        sub[1].append(record)
                        return
            # If subject doesn't exist, add it with the grade
                student[1].append([subject, [record]])
                return

        # If student doesn't exist, add the student and the subject with the grade
        self.gradebook.append([name, [[subject, [record]]]])        

    def calculate_average(self, name):
        for student in self.gradebook:
            if student[0] == name:
                total_sum = 0
                total_grades = 0
                for i in student[1]: #see the subjects
                    total_sum += sum(i[1])
                    total_grades += len(i[1])
                if total_grades>0:
                    return total_sum /total_grades
        return None

    def display_report(self):
        print("Gradebook Report:")
        for student in self.gradebook:
            print()
            print("\nStudent: " + student[0])
            for i in student[1]:
                grades = i[1]
                subject_average = sum(grades) / len(grades)
                print(f"  Subject: {i[0]}, Grades: {grades}, Average: {subject_average:.2f}")    

# Initialize an empty gradebook
gradebook = Gradebook()

# Add students
gradebook.add_student("Alice")
gradebook.add_student("Bob")

# Record grades
gradebook.record_grade("Alice", "Math", 85)
gradebook.record_grade("Alice", "Science", 92)
gradebook.record_grade("Bob", "Math", 78)
gradebook.record_grade("Bob", "Science", 88)
gradebook.record_grade("Alice", "Math", 90)  # Additional grade for Math


# Calculate average for a student
alice_avg = gradebook.calculate_average("Alice")
print(f"Alice's average grade: {alice_avg:.2f}")

# Calculate average for a student
bob_avg = gradebook.calculate_average("Bob")
print(f"Bob's average grade: {bob_avg:.2f}")

gradebook.display_report()
