from abc import ABC, abstractmethod
from memory.talk_memory import *
# from tools

class agent_base(ABC):

    def __init__(self,
                 database :Talk_Memory_,
                 
                 ):
        self.database = database
        self.model = 123
        