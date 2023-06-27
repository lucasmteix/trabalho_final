class GOTDatabase:

    def __init__(self, database):

        self.db = database

    def create_house(self, house):

        query = "CREATE (:House {name: $house_name})"
        parameters = {"house_name": house.name,}
        self.db.execute_query(query, parameters)

    def create_person(self, person):

        query = "CREATE (:Person {name: $person_name, age: $person_age})"
        parameters = {"person_name": person.name, "person_age": person.age}
        self.db.execute_query(query, parameters)

    def create_animal(self, animal):

        query = "CREATE (:Animal {species: $animal_species, name: $animal_name, age: $animal_age})"
        parameters = {"animal_species": animal.species, "animal_name": animal.name, "animal_age": animal.age}
        self.db.execute_query(query, parameters)

    def create_artifact(self, artifact):

        query = "CREATE (:Artifact {type: $artifact_type, name: $artifact_name, power: $artifact_power})"
        parameters = {"artifact_type": artifact.type, "artifact_name": artifact.name, "artifact_power": artifact.power}
        self.db.execute_query(query, parameters)

    def relate_house_person(self, house, person):

        query = "MATCH (h:House), (p:Person) WHERE h.name = $house_name AND p.name = $person_name " \
                "CREATE (p)-[r:INTEGRA]->(h)"
        parameters = {"house_name": house.name, "person_name": person.name}
        self.db.execute_query(query, parameters)

    def relate_person_animal(self, person, animal):

        query = "MATCH (p:Person), (a:Animal) WHERE p.name = $person_name AND a.name = $animal_name " \
                "CREATE (a)-[r:PERTENCE_A]->(p)"
        parameters = {"person_name": person.name, "animal_name": animal.name}
        self.db.execute_query(query, parameters)

    def relate_person_artifact(self, person, artifact):

        query = "MATCH (p:Person), (a:Artifact) WHERE p.name = $person_name AND a.name = $artifact_name " \
                "CREATE (a)-[r:POSSE_DE]->(p)"
        parameters = {"person_name": person.name, "artifact_name": artifact.name}
        self.db.execute_query(query, parameters)

    def retrieve_person(self, person):

        query = "MATCH (h:House)-[r]-(p:Person) WHERE p.name = $person_name RETURN p.age, h.name"
        parameters = {"person_name": person.name}
        result = self.db.execute_query(query, parameters)
        return result

    def update_person_age(self, person, new_age):

        query = "MATCH (p:Person) WHERE p.name = $person_name SET p.age = $new_age"
        parameters = {"person_name": person.name, "new_age": new_age}
        self.db.execute_query(query, parameters)

    def delete_person(self, person):

        query = "MATCH (p:Person) WHERE p.name = $person_name DETACH DELETE p"
        parameters = {"person_name": person.name}
        self.db.execute_query(query, parameters)