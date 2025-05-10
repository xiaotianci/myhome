from abc import ABC, abstractmethod
from memory.talk_memory import *
# from tools

class agent_base(ABC):

    def __init__(self,
                 database :Talk_Memory_,
                 
                 ):
        self.database = database
        self.model = 123

# class talk_agent(agent_base):
#     def __init__(self, database,memory):
#         super().__init__(database)
#         self.memory = memory
#         self.tools = 123
#         self.perception = 123
#         self.action = 123


# class talk_agent:
#     def __init__(self,memory, tools, perception,action):
#         self.memory = memory
#         self.tools = tools
#         self.perception = perception
#         self.action = action

#     def action(self):

# memory, tools, perception,action = '','','',''
# talk_agent(memory, tools, perception,action)