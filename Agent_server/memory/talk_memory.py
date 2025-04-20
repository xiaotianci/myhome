from schema import *
import uuid


class Talk_Memory_(Memory_):
    """
    情感交流记忆模块
        - 历史记录
        - 更新模块
        - 获取模块
    """
    def __init__(self):
        self.database()

    def database(self):
        self.database = []

    def get(self, *args):
        if len(args) == 1 and isinstance(args[0],int):
            "按照长度返回历史记录"
            history = self.database[:args[0]]
            return history
        
        

    # def get_by_date(self, len_history):
    #     pass

    # def get_by_(self, len_history):
    #     pass

    def update(self, talk_info : list[str,str]):
        user_talk = talk_info[0]
        system_talk = talk_info[1]
        self.database.append({'user_talk':user_talk,'system_talk':system_talk})

    def get_sentence_(input : str, role):
        unid = uuid.uuid4()
        date = data_()
        role = role
        sentence = input
        return sentence_(unid, date, role, sentence)
 


if __name__ == '__main__':
    talk_Memory = Talk_Memory_()
    print('请输入问题')
    user_talk = '天气如何'
    user_sentence = Talk_Memory_.get_sentence_(user_talk,'user_talk')

    system_talk = '今天天气不错'
    system_sentence = Talk_Memory_.get_sentence_(user_talk,'system_talk')
    
    talk_Memory.update([user_sentence,system_sentence])

    history = talk_Memory.get(5)