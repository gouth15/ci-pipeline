class Person:
    def __init__(self, fullname: str, age, occupation) -> None:
        self.fullname = fullname
        self.age = age
        self.occupation = occupation

    @property
    def get_forename(self):
        return self.fullname.split(" ")[0]
    
    @property
    def get_lastname(self):
        if len(self.fullname.split(" ")) == 1:
            return None
        else:
            return self.fullname.split()[1]
        
    def celebrate_birthday(self):
        self.age += 1
    
    def add_occupation(self, occupation):
        self.occupation.append(occupation)

    def __str__(self) -> str:
        return f"Name: {self.fullname}, Age: {self.age}, Occupation: {self.occupation}"

if __name__ == "__main__":
    people = Person("Carlos Sainz", 30, ["Formula 1 Driver"])
    print(people)
    first_name = people.get_forename
    last_name = people.get_lastname
    print(people.age)
    people.celebrate_birthday()
    print(people.age)
    people.add_occupation("Safety Car Driver")
    print(people)
