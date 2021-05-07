import db


class Professors:
    @staticmethod
    def add_professors(key_value: dict):
        """
        Add professor into database
        """
        db.Database.add('professors', key_value)

    @staticmethod
    def delete_professors(current_id: int):
        """
        Delete professor into database
        """
        db.Database.delete("professors", current_id)

    @staticmethod
    def show_all_professors():
        """
        Show all professor into database
        """
        return db.Database.show_table('professors')

    @staticmethod
    def show_all_professors_courses_and_students_count():
        """
         Show all professor courses and student count into database
        """
        return db.Database.show_all_professors_courses_and_students_count('students')

    @staticmethod
    def show_top_three_professors_enrolled_students_in_courses():
        """
        Shows a list of the first three teachers with
        the most enrolled students in all disciplines they teach
        """
        return db.Database.show_top_three_professors_enrolled_students_in_courses('students')


professor = Professors()