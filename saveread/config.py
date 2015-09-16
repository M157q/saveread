class Config():
    def __init__(self):
        self.config = {}
        self.config['db_path'] = "~/.config/saveread/saveread.db"

    def get_db_path(self):
        return self.config['db_path']
