


class Prompt_generation:
    def __init__(self,user_inputs, history):
        self.memory = 123
        return self.prompt_genetarion(user_inputs, history)



    def get_framework():
        framework = """
        <身份>你是一名情感交流专家，可以抚慰用户脆弱的心灵，给人以温暖</>
        <历史对话>{history}</>
        <用户问题>{user_input}</>
        <任务>现在你在跟用户进行交流，在<历史对话>中有你们的历史对话记录，请根据<历史对话>以及用户问题进行回答</>：
        """
        return framework

    def prompt_genetarion(self, user_inputs):
        pass