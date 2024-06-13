#coding:utf-8
"""
 Propriete: maniere de manipuler/controler des attributs
            principe d'encapsulation
"""
# class Humain:
#   def __init__(self,nom,age):
#     self.nom=nom
#     self.age=age

# #programme principale
# h1 = Humain('jason',25)

# print(h1.age)
# h1.age=1333
# print(h1.age)

class Person:
    def __init__(self, name, age):
        self.__name = name  # Attribut privé
        self.__age = age    # Attribut privé

    # Getter pour le nom
    def get_name(self):
        return self.__name

    # Setter pour le nom
    def set_name(self, name):
        self.__name = name

    # Getter pour l'âge
    def get_age(self):
        return self.__age

    # Setter pour l'âge
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be a positive number")

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

# Utilisation de la classe avec encapsulation
person = Person("Alice", 30)
print(person.get_name())  # Accès via getter
print(person.get_age())
person.set_age(31)        # Modification via setter
person.display_info()
