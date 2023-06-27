from database import Database
from got_database import GOTDatabase
from menu import Menu


# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.197.216.210:7687", "neo4j", "flags-rib-bow")
db.drop_all()

got_db = GOTDatabase(db)
menu = Menu(got_db)

menu.execute()

# Fechando a conexão
db.close()