class Course:
    def __init__(self, title, credit, teacher_id):
        self.title = title
        self.credit = credit
        self.teacher_id = teacher_id

    def db_data(self):
        return {"title": self.title, "credit": self.credit, "teacher_id": self.teacher_id}
