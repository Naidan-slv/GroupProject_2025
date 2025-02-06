class User:
    id: int
    username: str
    password: str
    first_name: str
    last_name: str

    def __init__(self, id, username, password, first_name, last_name):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
