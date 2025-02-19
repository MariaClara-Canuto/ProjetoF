from app.models.user_account import UserAccount
import json
import os

class DataRecord:
    def __init__(self):
        self.user_accounts = []
        try:
            # Caminho relativo para o arquivo JSON
            current_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(current_dir, "..", "controllers", "db", "user_accounts.json")
            
            with open(json_path, "r") as arquivo_json:
                user_data = json.load(arquivo_json)
                self.user_accounts = [UserAccount(**data) for data in user_data]
                self.limit = len(self.user_accounts) - 1
        except FileNotFoundError:
            self.user_accounts.append(UserAccount('Guest', '000000'))
            self.limit = 0

    def work_with_parameter(self, parameter):
        try:
            index = int(parameter)
            if 0 <= index <= self.limit:
                return self.user_accounts[index]
            else:
                return None
        except ValueError:
            return None