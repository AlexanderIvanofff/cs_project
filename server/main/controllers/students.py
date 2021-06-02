from ..helpers import db
from ..models.student import Student


class Students:
    @staticmethod
    def add_student(data: dict):
        """
        Add students into database
        """
        student = Student(data.first_name, data.last_name, data.course_id)
        db.Database.add("students", student.db_data())

    @staticmethod
    def delete_student(current_id: int):
        """
        Delete students into database
        """
        db.Database.delete("students", current_id)

    @staticmethod
    def update(course_id: int, student_id: int):
        """
        Change student course
        """
        db.Database.edit('students', 'course_id', course_id, student_id)