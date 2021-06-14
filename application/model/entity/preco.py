class Preco:
    def __init__(self, parcela:int, valorParcela:float, valorAvista:float ):
        self.__parcela = parcela
        self.__valorParcela= valorParcela
        self.__valorAvista = valorAvista
        
    @property
    def parcela(self):
        return self.__parcela
    
    @property
    def valorParcela(self):
        return self.__valorParcela
    
    @property
    def valorAvista(self):
        return self.__valorAvista
        