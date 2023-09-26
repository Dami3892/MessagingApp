# Example application/service layer

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate_user(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if user and user.password == password:
            return True
        return False

    def create_user(self, username, password, email):
        # Perform validation, business logic, and data operations
        user = User(username, password, email)
        self.user_repository.save_user(user)
        return user

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def update_user_email(self, user_id, email):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            user.email = email
            self.user_repository.save_user(user)
            return True
        return False

    def delete_user(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            self.user_repository.delete_user(user)
            return True
        return False


class UserRepository:
    def get_user_by_id(self, user_id):
        # Retrieve user from data layer (e.g., database)
        pass

    def get_user_by_username(self, username):
        # Retrieve user from data layer by username
        pass

    def save_user(self, user):
        # Save user to data layer (e.g., database)
        pass

    def delete_user(self, user):
        # Delete user from data layer
        pass


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
