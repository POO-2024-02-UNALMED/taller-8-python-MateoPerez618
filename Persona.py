class Persona:
    def __init__(self, nombre: str, edad: int, altura: str, sexo: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__sexo = sexo

    def get_nombre(self) -> str:
        return self.__nombre

    def get_edad(self) -> int:
        return self.__edad

    def get_altura(self) -> str:
        return self.__altura

    def get_sexo(self) -> str:
        return self.__sexo
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_edad(self, edad: int):
        self.__edad = edad

    def set_altura(self, altura: str):
        self.__altura = altura

    def set_sexo(self, sexo: str):
        self.__sexo = sexo