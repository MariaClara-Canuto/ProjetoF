from app.models.user_account import UserAccount
import json
import os

class DataRecord:
    def __init__(self):
        self.user_accounts = []
        self.json_path = self._get_json_path()
        self._load_users()


    def _get_json_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "..", "controllers", "db", "user_accounts.json")
        return json_path

    def work_with_parameter(self, parameter):
        try:
            index = int(parameter)
            if 0 <= index <= self.limit:
                return self.user_accounts[index]
            else:
                return None
        except ValueError:
            return None

    def _load_users(self):
        try:
            with open(self.json_path, "r") as arquivo_json:
                user_data = json.load(arquivo_json)
                self.user_accounts = [UserAccount(**data) for data in user_data]
                self.limit = len(self.user_accounts) - 1
                
        except FileNotFoundError:
            self.user_accounts.append(UserAccount('Guest', '000000'))
            self.limit = 0

    def _save_users(self):
        with open(self.json_path, 'w') as arquivo_json:
            json.dump([user.__dict__ for user in self.user_accounts], arquivo_json, ident=4)

    def add_user(self, username, password):
        new_user = UserAccount(username, password)
        self.user_account.append(new_user)
        self._save_users()

        return f'Usuário: {username} adicionado com sucesso!'

    def find_user(self):
        for user in self.user_accounts:
            if user.username == username and user.password == password:
                return user
            
        return None