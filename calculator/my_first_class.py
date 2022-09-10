from codecs import getencoder


class Person:
    age = 0
    gender = 0
    name = 0
    def talk(self):
        if self.name != 0:
            print(f"hi mi name is {self.name}")
        else:
            print("error. must have a name")

Lucas = Person()
print(Lucas.name)
Lucas.talk()
Lucas.name = "xah3o" 
print(Lucas.name)
Lucas.talk()
