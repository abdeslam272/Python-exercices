class Gradebook:
    def __init__(self):
        self.gradebook = []
        
    def find_gradebook(self, name):
        for student in self.gradebook:
            if student[0] == name in self.gradebook:
                return name
        return None

    def add_student(self,name):
        grades = [name, []]
        self.gradebook.append(grades)

    def record_grade(self,name,subject,record):
        student_exist = False
        for student in self.gradebook:
            if student[0] == name in self.gradebook:
                subject = [subject, record]
                student[1].append(subject)
                student = True
        if student_exist == False:
            gradebook = [name, [subject, record]]
            self.gradebook.append(gradebook)
            

    def display_report(self):
        print("Gradebook Report:")
        for student in self.gradebook:
            print("Student: " + student[0])
            print("Subject: " + str(student[1]))
    

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
gradebook.display_report()