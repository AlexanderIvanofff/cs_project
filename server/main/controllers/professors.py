from ..models.professors_model import ProfessorModel

model = ProfessorModel()


class Professors:
    @staticmethod
    def add_professors(data: dict):
        model.add(data)

    @staticmethod
    def delete_professors(current_id: int):
        model.delete(current_id)

    @staticmethod
    def show_all_professors():
        return model.show_all_professors()
