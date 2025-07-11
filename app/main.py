class Person:
    people = {"name": None, "person": None}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({"name": self.name, "person": self})


def create_person_list(people: list) -> list:
    # write your code here
    pass
