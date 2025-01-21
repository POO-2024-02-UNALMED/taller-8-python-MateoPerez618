class Deportista:
    def __init__(self, deporte: str = "Futbol", añosPracticando: int = 0):
        self.__deporte = deporte
        self.__añosPracticando = añosPracticando

    def getDeporte(self) -> str:
        return self.__deporte

    def getAñosPracticando(self) -> int:
        return self.__añosPracticando
    
    def setDeporte(self, deporte: str):
        self.__deporte = deporte

    def setAñosPracticando(self, añosPracticando: int):
        self.__añosPracticando = añosPracticando