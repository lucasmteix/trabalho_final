class House:

    def __init__(self, name=None, persons=None):

        self.name = name
        self.persons = persons or []


class Person:

    def __init__(self, name, age=None, animals=None, artifacts=None):

        self.name = name
        self.age = age
        self.animals = animals or []
        self.artifacts = artifacts or []


class Animal:

    def __init__(self, species=None, name=None, age=None):

        self.species = species
        self.name = name
        self.age = age


class Artifact:

    def __init__(self, type, name, power):

        self.type = type
        self.name = name
        self.power = power