from ..models.students_model import StudentModel

model = StudentModel()


class Students:
    @staticmethod
    def add_student(data: dict):
        model.add(data)

    @staticmethod
    def delete_student(current_id: int):
        model.delete_student(current_id)

    @staticmethod
    def update(course_id: int, student_id: int):
        model.update(course_id, student_id)
        # db.Database.edit('students', 'course_id', course_id, student_id)
