class Deportista:
    def __init__(self, deporte: str = "Fútbol", añosPracticando: int = 0):
        self.__deporte = deporte
        self.__añosPracticando = añosPracticando

    def get_deporte(self) -> str:
        return self.__deporte

    def get_añosPracticando(self) -> int:
        return self.__añosPracticando
    
    def set_deporte(self, deporte: str):
        self.__deporte = deporte

    def set_añosPracticando(self, añosPracticando: int):
        self.__añosPracticando = añosPracticando