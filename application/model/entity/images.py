class Images:
    def __init__(self, link:str):
        self.__link = link
    
    @property
    def link(self):
        return self.__link