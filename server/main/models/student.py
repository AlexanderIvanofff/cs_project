class Student:
    def __init__(self, first_name, last_name, course_id):
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id

    def db_data(self):
        return {"first_name": self.first_name, "last_name": self.last_name, "course_id": self.course_id}