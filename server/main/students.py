import db


class Students:
    @staticmethod
    def add_student(key_values: dict):
        """
        Add students into database
        """
        db.Database.add("students", key_values)

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

    @staticmethod
    def show_all_students_and_there_courses():
        """
        Shows all students and courses they have enrolled
        """
        return db.Database.show_all_students_and_there_courses('students')


student = Students()