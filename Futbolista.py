from Persona import Persona
from Deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre: str, edad: int, altura: str, sexo: str, añosPracticando: int = 0, golesMarcados: int = 0, tarjetasRojas: int = 0, piernaHabil: str = "Desconocida", deporte: str = "Fútbol"):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando)
        
        self.__golesMarcados = golesMarcados
        self.__tarjetasRojas = tarjetasRojas
        self.__piernaHabil = piernaHabil

        Futbolista.listaFutbolistas.append(self)

    def get_golesMarcados(self) -> int:
        return self.__golesMarcados

    def get_tarjetasRojas(self) -> int:
        return self.__tarjetasRojas

    def get_piernaHabil(self) -> str:
        return self.__piernaHabil

    def set_golesMarcados(self, golesMarcados: int):
        self.__golesMarcados = golesMarcados

    def set_tarjetasRojas(self, tarjetasRojas: int):
        self.__tarjetasRojas = tarjetasRojas

    def set_piernaHabil(self, piernaHabil: str):
        self.__piernaHabil = piernaHabil

    def __str__(self) -> str:
        return (f"Mi nombre es {self.get_nombre()} soy profesional en el deporte {self.get_deporte()} "
                f"Tengo {self.get_edad()} años de edad y llevo {self.get_añosPracticando()} años en el deporte")
    
futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
print(futbolista)