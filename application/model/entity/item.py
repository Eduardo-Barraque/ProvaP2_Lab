from application.model.entity.images import Images
from typing import List
class Item:
    def __init__(self, id:int, nome:str, lista_imagens: List[Images], parcela:int, valorParcela:float, valorAvista:float ):
        self.__nome = nome
        self.__id = id
        self.__lista_imagens = lista_imagens
        self.__parcela = parcela
        self.__valorParcela= valorParcela
        self.__valorAvista = valorAvista
        
    
    @property
    def id(self):
        return self.__id
    
    
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def lista_imagens(self):
        return self.__lista_imagens

    @property
    def parcela(self):
        return self.__parcela
    
    @property
    def valorParcela(self):
        return self.__valorParcela
    
    @property
    def valorAvista(self):
        return self.__valorAvista