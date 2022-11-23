# Importa nosso arquivo Pessoa.py no dirtório model
from model.Pessoa import Pessoa

# Exemplo de uso
guimaraes = Pessoa(1, "Alyson Guimarães")
print(guimaraes)

# Mostrar somente o nome ou o id
print(guimaraes.nome)
print(guimaraes.id)

