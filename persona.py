class Persona:
    def __init__(self, nombre: str, edad: int, altura: str, sexo: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__sexo = sexo

    def getNombre(self) -> str:
        return self.__nombre

    def getEdad(self) -> int:
        return self.__edad

    def getAltura(self) -> str:
        return self.__altura

    def getSexo(self) -> str:
        return self.__sexo
    
    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setEdad(self, edad: int):
        self.__edad = edad

    def setAltura(self, altura: str):
        self.__altura = altura

    def setSexo(self, sexo: str):
        self.__sexo = sexo