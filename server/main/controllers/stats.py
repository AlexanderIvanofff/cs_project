from ..models.model_stats import StatsModel


class Stats:
    @staticmethod
    def show_top_three_courses():
        """
        Displays a list of the first three subjects with
        the most enrolled students
        """
        return StatsModel.show_top_three_courses("courses")

    @staticmethod
    def show_all_professors_courses_and_students_count():
        """
         Show all professor courses and student count into database
        """
        return StatsModel.show_all_professors_courses_and_students_count('students')

    @staticmethod
    def show_top_three_professors_enrolled_students_in_courses():
        """
        Shows a list of the first three teachers with
        the most enrolled students in all disciplines they teach
        """
        return StatsModel.show_top_three_professors_enrolled_students_in_courses('students')

    @staticmethod
    def show_all_students_and_there_courses():
        """
        Shows all students and courses they have enrolled
        """
        return StatsModel.show_all_students_and_there_courses('students')

