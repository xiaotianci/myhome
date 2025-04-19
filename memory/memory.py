from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class talk_current:
    systrm_talk : str
    user_talk : str

@dataclass
class talk_history:
    systrm_talk : list[dict]
    user_talk : list[dict]

class Memory(ABC):
    def __init__(self,**config):
        self.config = config
    
    @abstractmethod
    def get(**args):
        pass

    @abstractmethod
    def update(**args):
        pass

    @abstractmethod
    def database(**args):
        pass

    def __call__(self, **args):
        return self.get(**args)



class Talk_Memory(Memory):
    """
    情感交流记忆模块
        - 历史记录
        - 更新模块
        - 获取模块
    """

    def database(**args):
        pass

    def get(self, len_history):
        pass

    def update(self, talk_info : talk_current):
        
        pass
 
