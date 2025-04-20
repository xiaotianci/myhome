from abc import ABC, abstractmethod
from dataclasses import dataclass
import datetime
import uuid
from config import *

class data_ :
    def __init__(self):
        self.current_data()

    def current_data(self):
        current_datetime = datetime.datetime.now()

        # 获取年、月、日、小时、分钟
        self.year = current_datetime.year
        self.month = current_datetime.month
        self.day = current_datetime.day
        self.hour = current_datetime.hour
        self.minute = current_datetime.minute

@dataclass
class sentence_:
    uuid : uuid
    date : data_
    role : str
    sentence : str

    def __post_init__(self):
        if self.role not in ROLE:
            raise ValueError("unknow role, role must be either 'systrm_talk' or 'user_talk'")

# @dataclass
# class talk_current_:
#     systrm_talk : str
#     user_talk : str

# @dataclass
# class talk_history_:
#     systrm_talk : list[dict]
#     user_talk : list[dict]



class Memory_(ABC):
    def __init__(self,**config):
        self.config = config
    
    @abstractmethod
    def get(**args):
        "获取历史记录"

    @abstractmethod
    def update(**args):
        pass

    @abstractmethod
    def database(**args):
        pass

    def __call__(self, **args):
        return self.get(**args)