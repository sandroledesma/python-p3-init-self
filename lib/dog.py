#!/usr/bin/env python3

class Dog:
    def __init__(self, name="Mutt", breed="Mutt"):
        self.name = name
        self.breed = breed
    
    def bark(self): 
        print("Woof!")

    def get_adopted(self, owner_name):
        self.owner = owner_name

fido = Dog("Fido")

snoopy = Dog("Snoopy")