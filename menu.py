from model import *
from got_database import GOTDatabase

class Menu:

    def __init__(self, got_db: GOTDatabase):
        self.got_db = got_db

    def execute(self):

        flag = 1
        operacao = 0

        while (flag == 1):

            print("SISTEMA DE CONSULTA AO BANCO DE DADOS DE GAME OF THRONES")
            print("Operações:")
            print("1 - inserir algo novo no banco de dados")
            print("2 - pesquisar algo no banco de dados")
            print("3 - atualizar algo no banco de dados")
            print("4 - deletar algo no banco de dados")

            operacao = int(input("Digite o número da operação desejada: "))

            print("Suboperações:")

            if(operacao == 1):
                self.create_menu()

            elif(operacao == 2):
                self.retrieve_menu()

            elif(operacao == 3):
                self.update_menu()

            elif(operacao == 4):
                self.delete_menu()

            flag = int(input("Deseja fazer mais uma operação? Digite 1 para sim e 0 para não: "))

    def create_menu(self):

        suboperacao = 0

        print("1 - inserir uma casa")
        print("2 - inserir uma pessoa")
        print("3 - inserir um animal")
        print("4 - inserir um artefato")
        print("5 - relacionar uma pessoa a uma casa")
        print("6 - relacionar um animal a uma pessoa")
        print("7 - relacionar um artefato a uma pessoa")

        suboperacao = int(input("Digite o número da suboperação desejada: "))

        if(suboperacao == 1):

            self.create_house_menu()

        elif(suboperacao == 2):

            self.create_person_menu()

        elif(suboperacao == 3):

            self.create_animal_menu()

        elif(suboperacao == 4):

            self.create_artifact_menu()

        elif(suboperacao == 5):

            self.relate_house_person_menu()

        elif(suboperacao == 6):

            self.relate_person_animal_menu()

        elif(suboperacao == 7):

            self.relate_person_artifact_menu()

    def create_house_menu(self):

        print("Inserindo uma nova casa...")

        house = House(input("Insira o nome da casa: "))

        self.got_db.create_house(house)
    def create_person_menu(self):

        print("Inserindo uma nova pessoa...")

        person = Person(input("Insira o nome da pessoa: "), input("Insira a idade da pessoa: "))

        self.got_db.create_person(person)

        tem_animais = input("Essa pessoa tem animais? Digite S para sim e N para não: ")

        if tem_animais == 'S':

            animal_quantity = int(input("Quantos? "))

            for i in range(animal_quantity):

                animal = self.create_animal_menu()
                person.animals.append(animal)
                self.got_db.relate_person_animal(person, animal)
        else:

            print("Você selecionou que a pessoa não tem animais.")

        tem_artefatos = input("Essa pessoa tem artefatos? Digite S para sim e N para não: ")

        if tem_artefatos == 'S':

            artifacts_quantity = int(input("Quantos? "))

            for i in range(artifacts_quantity):

                artifact = self.create_artifact_menu()
                person.artifacts.append(artifact)
                self.got_db.relate_person_artifact(person, artifact)
        else:

            print("Você selecionou que a pessoa não tem artefatos.")

    def create_animal_menu(self):

        print("Inserindo um novo animal...")

        animal = Animal(input("Insira a espécie do animal: "), input("Insira o nome do animal: "),
                        int(input("Insira a idade do animal: ")))

        self.got_db.create_animal(animal)

        return animal

    def create_artifact_menu(self):

        print("Inserindo um novo artefato...")

        artifact = Artifact(input("Insira o tipo do artefato: "), input("Insira o nome do artefato: "),
                            int(input("Insira o poder do artefato: ")))

        self.got_db.create_artifact(artifact)

        return artifact

    def relate_house_person_menu(self):

        print("Relacionando uma pessoa a uma casa...")

        house = House(input("Insira o noma da casa: "))
        person = Person(input("Insira o nome da pessoa: "))

        self.got_db.relate_house_person(house, person)

    def relate_person_animal_menu(self):

        print("Relacionando um animal a uma pessoa...")

        animal = Animal(None, input("Insira o nome do animal: "))
        person = Person(input("Insira o nome da pessoa: "), None)
        self.got_db.relate_person_animal(person, animal)

    def relate_person_artifact_menu(self):

        print("Relacionando um artefato a uma pessoa...")

        artifact = Artifact(None, input("Insira o nome do artefato: "), None)
        person = Person(input("Insira o nome da pessoa: "), None)
        self.got_db.relate_person_artifact(person, artifact)

    def retrieve_menu(self):

        suboperacao = 0

        print("1 - pesquisar os dados de uma pessoa")

        suboperacao = int(input("Digite o número da suboperação desejada: "))

        if(suboperacao == 1):
            self.retrieve_person_menu()

    def retrieve_person_menu(self):

        print("Pesquisando os dados de uma pessoa...")

        person = Person(input("Insira o nome da pessoa: "))

        result = self.got_db.retrieve_person(person)

        print(result)

    def update_menu(self):

        suboperacao = 0

        print("1 - atualizar a idade de uma pessoa")

        suboperacao = int(input("Digite o número da suboperação desejada: "))

        if(suboperacao == 1):
            self.update_person_age_menu()

    def update_person_age_menu(self):

        print("Atualizando a idade de uma pessoa...")

        person = Person(input("Insira o nome da pessoa: "))

        new_age = input("Insira a nova idade: ")

        self.got_db.update_person_age(person, new_age)

        print("Idade atualizada.")

    def delete_menu(self):

        suboperacao = 0

        print("1 - deletar uma pessoa")

        suboperacao = int(input("Digite o número da suboperação desejada: "))

        if(suboperacao == 1):
            self.delete_person_menu()

    def delete_person_menu(self):

        print("Deletando uma pessoa...")

        person = Person(input("Insira o nome da pessoa: "))

        self.got_db.delete_person(person)

        print("Pessoa deletada.")
