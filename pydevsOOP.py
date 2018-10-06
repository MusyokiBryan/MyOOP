class Humans:
    def __init__(self, name, race, gender, age):
        self.name = name
        self.race = race
        self.gender = gender
        self.age = age

    def description(self):
        return 'Name:{}, race:{},  gender:{}, age:{}'.format(self.name, self.race, self.gender, self.age)

    def _talk(self, language):
        return 'A Kenyan speaks {}'.format(language)


class Women(Humans):
    def run (self, color):
        return "{} {} {} {}".format(self.name,self.race, self.age, color)

    # def _init_(self, name, race, gender, age, color):
    #     self.color = color
    #     super()._init_(name, race, gender, age)


# class Men(Humans):
#     def _init_(self, name, race, gender, age, height):
#         self.height = height
#         super()._init_(name, race, gender, age)


human1 = Humans('Maggie', 'Black', 'Female', 25)
human2 = Women('Sylvia', 'Caucasian',380)
# human3 = Men('Ben', 'British', 'Male', 40, '6feet')
print(human1.description())
print(human1._talk('Kiswahili'))
print(human2.run("red"))