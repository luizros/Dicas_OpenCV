class Pessoa:
    def __init__(self: object, nome: str, cpf: int, dataNascimento: int)->None:
        self.__nome = nome
        self.__cpf = cpf
        self.__dataNascimento = dataNascimento
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def concatena(self: object, n: str):
        nome , sobrenome = n
        self.__nome = self.__nome + ' ' + nome + ' '+ sobrenome
        return self.__nome
        
class Aluno
        