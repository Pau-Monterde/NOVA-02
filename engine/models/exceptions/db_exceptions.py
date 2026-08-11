class UserNotFound(Exception):
    def __init__(self):
        super().__init__(f"There isn'n any user in DB")