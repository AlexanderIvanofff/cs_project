from ..helpers import db


class CourseModel:
    @staticmethod
    def add(data):
        """
        Add course into database
        """
        course = Course(data["title"], data["credits"], data["professor_id"])
        return db.Database.add('courses', course.db_data())

    @staticmethod
    def delete(current_id):
        """
        Delete course into database
        """
        db.Database.delete("courses", current_id)

    @staticmethod
    def show_all_courses():
        """
        Show all title into database
        """
        return db.Database.show_table("courses")


class Course:
    def __init__(self, title, credit, teacher_id):
        self.title = title
        self.credit = credit
        self.teacher_id = teacher_id

    def db_data(self):
        return {"title": self.title, "credits": self.credit, "professor_id": self.teacher_id}
