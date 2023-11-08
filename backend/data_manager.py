class DataManager:
    def __init__(self):
        self.crypto_data = {}

    def update_data(self, data):
        self.crypto_data = data

    def get_data(self):
        return self.crypto_data