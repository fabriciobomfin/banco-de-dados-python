import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com o banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session() 

# Criando Tabela
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# CRUS.
# Create - Insert - Salvar.
os.system("clear")  # Limpar a tela
print("Solicitando dados ao usuário.")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu e-mail: ")
inserir_senha = input("Digite sua senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(cliente)
session.commit()

# Read - Select - Consulta
print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

session.close()

'''# Update - Atualizar
print("\nAtualizando dados do usuário.")
email_cliente = input("Digite o e-mail do cliente que deseja atualizar: ")
cliente = session.query(Cliente).filter_by(email=email_cliente).first()

if cliente:
    cliente.nome = input("Digite o novo nome: ")
    cliente.email = input("Digite o novo e-mail: ")
    cliente.senha = input("Digite a nova senha: ")
    session.commit()
    print("Dados atualizados com sucesso.")
else:
    print("Cliente não encontrado.")

# Fechar sessão
session.close()

#D - Delete - DELETE -EXcluir
print("\nExcluindo os dados de um cliente.")
email_cliente = session.query(cliente).filter_by(email_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente{cliente.nome} excluido com sucesso!")
else:
    print("Cliente não encontrado.")

    '''

#R - Read - SELECT - Consulta
