class Settings:
    def __init__(self):
        with open("settings.properties", "r") as f:
            self.repo_type = f.readline().strip().split(" ")[2]
            self.movies_file = f.readline().strip().split(" ")[2]
            self.client_file = f.readline().strip().split(" ")[2]
            self.rental_file = f.readline().strip().split(" ")[2]