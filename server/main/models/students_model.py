from ..helpers import db


class StudentModel:
    @staticmethod
    def add(data):
        """
        Add students into database
        """
        student = Student(data["first_name"], data["last_name"], data["course_id"])
        return db.Database.add("students", student.db_data())

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


class Student:
    def __init__(self, first_name, last_name, course_id):
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id

    def db_data(self):
        return {"first_name": self.first_name, "last_name": self.last_name, "course_id": self.course_id}
