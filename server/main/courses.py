import db


class Courses:
    @staticmethod
    def add_courses(key_value: dict):
        """
        Add courses into database
        """
        db.Database.add('courses', key_value)

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

    @staticmethod
    def show_top_three_courses():
        """
        Displays a list of the first three subjects with
        the most enrolled students
        """
        return db.Database.show_top_three_courses("courses")


courses = Courses()