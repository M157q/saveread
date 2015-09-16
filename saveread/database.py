class SavereadDB():
    def __init__(self):
        from saveread import config
        config = config.Config()

        self.path = config.get_db_path()
