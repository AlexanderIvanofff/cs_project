from ..helpers import db
from ..models.course import Course


class Courses:
    @staticmethod
    def add_courses(data: dict):
        """
        Add courses into database
        """
        course = Course(data["title"], data["credits"], data["professor_id"])
        db.Database.add('courses', course.db_data())

    @staticmethod
    def delete_courses(current_id: int):
        """
        Delete course from database
        """
        db.Database.delete("courses", current_id)

    @staticmethod
    def show_all_courses():
        """
        Show all title into database
        """
        return db.Database.show_table("courses")
