from ..models.courses_model import CourseModel

model = CourseModel()


class Courses:
    @staticmethod
    def add_courses(data: dict):
        model.add(data)

    @staticmethod
    def delete_courses(current_id: int):
        model.delete(current_id)

    @staticmethod
    def show_all_courses():
        return model.show_all_courses()
