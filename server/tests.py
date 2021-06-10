import unittest

from main.models.courses_model import Course, CourseModel
from main.models.professors_model import Professor, ProfessorModel
from main.models.students_model import Student, StudentModel
from main.models.title_models import Title, TitleModel
from unittest import mock


class CourseTest(unittest.TestCase):
    def setUp(self):
        self.course = Course("data_base", 5, 6)

    def test_course_is_properly_initiated(self):
        self.assertEqual(self.course.title, "data_base")
        self.assertEqual(self.course.credit, 5)
        self.assertEqual(self.course.teacher_id, 6)

    def test_db_data_get_correct_data(self):
        self.assertEqual(self.course.db_data(), {"credits": 5, "professor_id": 6, "title": "data_base"})


class ProfessorTest(unittest.TestCase):
    def setUp(self):
        self.professor = Professor("Alexander", "Ivanov")

    def test_course_is_properly_initiated(self):
        self.assertEqual(self.professor.first_name, "Alexander")
        self.assertEqual(self.professor.last_name, "Ivanov")

    def test_db_data_get_correct_data(self):
        self.assertEqual(self.professor.db_data(), {"first_name": "Alexander", "last_name": "Ivanov"})


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.student = Student("Alexander", "Ivanov", 5)

    def test_course_is_properly_initiated(self):
        self.assertEqual(self.student.first_name, "Alexander")
        self.assertEqual(self.student.last_name, "Ivanov")
        self.assertEqual(self.student.course_id, 5)

    def test_db_data_get_correct_data(self):
        self.assertEqual(self.student.db_data(), {"first_name": "Alexander", "last_name": "Ivanov", "course_id": 5})


class TitleTest(unittest.TestCase):
    def setUp(self):
        self.title = Title("Python")

    def test_course_is_properly_initiated(self):
        self.assertEqual(self.title.title_name, "Python")

    def test_db_data_get_correct_data(self):
        self.assertEqual(self.title.db_data(), {"title_name": "Python"})


class TitleModelTest(unittest.TestCase):
    def test_title_add(self):
        with unittest.mock.patch('main.models.title_models.TitleModel.add',
                                 return_value=[
                                     {"title_name": "title_name"}]):
            result = TitleModel.add()
            self.assertEqual(result, [{
                "title_name": "title_name"
            }])

    def test_title_delete(self):
        with unittest.mock.patch('main.models.title_models.TitleModel.delete_title',
                                 return_value=[
                                     {"current_id": "current_id"}]):
            result = TitleModel.delete_title()
            self.assertEqual(result, [{
                "current_id": "current_id"
            }])

    def test_is_title_return_all_titles_form_db(self):
        self.assertEqual(TitleModel.show_all_titles(), [(1, 'Associate Professor'),
                                                        (2, 'Associate Professor'),
                                                        (60, 'DOCENT PROFESSOR')])


class StudentModelTest(unittest.TestCase):
    def test_student_add(self):
        with unittest.mock.patch('main.models.students_model.StudentModel.add',
                                 return_value=[
                                     {"first_name": "first_name", "last_name": "last_name", "course_id": "course_id"}]):
            result = StudentModel.add()
            self.assertEqual(result, [{
                "first_name": "first_name", "last_name": "last_name", "course_id": "course_id"
            }])

    def test_student_delete(self):
        with unittest.mock.patch('main.models.students_model.StudentModel.delete_student',
                                 return_value=[
                                     {"current_id": "current_id"}]):
            result = StudentModel.delete_student()
            self.assertEqual(result, [{
                "current_id": "current_id"
            }])

    def test_update_student(self):
        with unittest.mock.patch('main.models.students_model.StudentModel.update',
                                 return_value=[
                                     {"course_id": "course_id", "student_id": "student_id"}]):
            result = StudentModel.update()
            self.assertEqual(result, [
                {'course_id': 'course_id', 'student_id': 'student_id'}
            ])


class ProfessorModelTest(unittest.TestCase):
    def test_professor_add(self):
        with unittest.mock.patch('main.models.professors_model.ProfessorModel.add',
                                 return_value=[{'first_name': 'first_name', "last_name": "last_name"}]):
            result = ProfessorModel.add()
            self.assertEqual(result, [{
                "first_name": "first_name", "last_name": "last_name"
            }])

    def test_professor_delete(self):
        with unittest.mock.patch('main.models.professors_model.ProfessorModel.delete',
                                 return_value=[{'current_id': 'current_id'}]):
            result = ProfessorModel.delete()
            self.assertEqual(result, [{
                "current_id": "current_id"
            }])

    def test_is_professor_return_all_professors_form_db(self):
        self.assertEqual(ProfessorModel.show_all_professors(), [(7, 'Angel', 'Grablev', 1),
                                                                (9, 'Yano', 'Petkov', 1),
                                                                (13, 'Doncho', 'Minkov', 1),
                                                                (14, 'Borislav', 'Georgiev', 2)])


class CourseModelTest(unittest.TestCase):
    def test_course_add(self):
        with unittest.mock.patch('main.models.courses_model.CourseModel.add', return_value=[{'title': 'title'}]):
            result = CourseModel.add()
            self.assertEqual(result, [{
                "title": "title"
            }])

    def test_course_delete(self):
        with unittest.mock.patch('main.models.courses_model.CourseModel.delete',
                                 return_value=[{'current_id': 'current_id'}]):
            result = CourseModel.delete()
            self.assertEqual(result, [{
                "current_id": "current_id"
            }])

    def test_is_course_return_all_courses_form_db(self):
        self.assertEqual(CourseModel.show_all_courses(), [(2, 'Database Design', '10', 5),
                                                          (3, 'Python Engineer', '10', 9),
                                                          (4, 'Django Web', '15', 10),
                                                          (6, 'Reactjs', '25', 5),
                                                          (7, 'C# Advanced', '8', 11),
                                                          (12, 'Flask', '15', 7),
                                                          (13, 'Scrum', '8', 9)])


if __name__ == '__main__':
    unittest.main()
