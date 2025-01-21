from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre: str, edad: int, altura: str, sexo: str, añosPracticando: int = 0, golesMarcados: int = 0, tarjetasRojas: int = 0, piernaHabil: str = "Desconocida", deporte: str = "Futbol"):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando)
        
        self.__golesMarcados = golesMarcados
        self.__tarjetasRojas = tarjetasRojas
        self.__piernaHabil = piernaHabil

        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self) -> int:
        return self.__golesMarcados

    def getTarjetasRojas(self) -> int:
        return self.__tarjetasRojas

    def getPiernaHabil(self) -> str:
        return self.__piernaHabil

    def setGolesMarcados(self, golesMarcados: int):
        self.__golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas: int):
        self.__tarjetasRojas = tarjetasRojas

    def setPiernaHabil(self, piernaHabil: str):
        self.__piernaHabil = piernaHabil

    def __str__(self) -> str:
        return (f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} "
                f"Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte")
    
futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
print(futbolista)