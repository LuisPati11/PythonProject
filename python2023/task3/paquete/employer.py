class Employer:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    @staticmethod
    def show_employers(employers):
        for employer in employers:
            print(f"Name: {employer.name} - Location: {employer.location}")

    