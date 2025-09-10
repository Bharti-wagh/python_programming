#Create class 'pets' from a class "animal" and further create class "dog" from "pets".
# add a meethod "bark" to class "Dog"
class animal:
    pass
class pets(animal):
    pass
class dog:
    @staticmethod
    def bark():
        print("Dog is bark")

d=dog()
d.bark()