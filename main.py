# Importa nosso arquivo Pessoa.py no dirtório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

# Exemplo de uso
guimaraes = Pessoa(1, "Alyson Guimarães")
print(guimaraes)

# Mostrar somente o nome ou o id
print(guimaraes.nome)
print(guimaraes.id)

print("Daqui pra frente é acesso ao banco de dados.")
# Chama objeto de banco de dados
db = Database()

# Instancia o objeto 
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

# Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(True)
for pessoa in pessoas:
  print(pessoa)
