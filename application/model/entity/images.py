class Images:
    def __init__(self, id:int, link:str):
        self.__link = link
        self.__id = id
    
    @property
    def link(self):
        return self.__link
    
    @property
    def id(self):
        return self.__id