from ..models.title_models import TitleModel

model = TitleModel()


class Titles:
    @staticmethod
    def add_title(data: dict):
        model.add(data)

    @staticmethod
    def delete_title(current_id: int):
        model.delete_title(current_id)

    @staticmethod
    def show_all_titles():
        return model.show_all_titles()
