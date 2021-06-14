from application.model.entity.images import Images
from application.model.entity.preco import Preco
from typing import List
class Item:
    def __init__(self, id, nome, lista_imagens: List[Images],valores: List[Preco] ):
        self.__nome = nome
        self.__id = id
        self.__lista_imagens = lista_imagens
        self.__valores = valores
    
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
    def valores(self):
        return self.__valores