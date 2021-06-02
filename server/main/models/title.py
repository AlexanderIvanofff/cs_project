class Title:
    def __init__(self, title_name):
        self.title_name = title_name

    def db_data(self):
        return {"title_name": self.title_name}