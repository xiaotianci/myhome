import requests
from abc import ABC, abstractmethod
from generate_prompt.prompte_generation import Prompt_generation 
from config import *


class Models(ABC):
    def __init__(
            self,
            prompt_generation : Prompt_generation,
            private_models_url : Models_url,
            ):
          
        self.prompt_generation = prompt_generation
        self._private_models_url = private_models_url
        self.models = list(self._private_models_url.keys())
    
    def is_support(self, model_name):
        if f'{model_name}_url' not in self.models:
                raise "模型不可用"

    def get_url(self, model_name):
        return self._private_models_url[f'{model_name}_url']

    @abstractmethod
    def infer(self, question):
        pass

    def __call__(self, question):
        return self.infer(question)


class GPT2_model(Models):
    def __init__(self, prompt_generation:Prompt_generation, private_models_url:Models_url, model_name='gpt2'):
        super().__init__(prompt_generation, private_models_url)
        self.model_name = model_name
    
    def infer(self, question):
        self.is_support(self.model_name)
        url = self.get_url(self.model_name)
        question = self.prompt_generation.prompt_genetarion(question)

        data = {"question": question}
        response = requests.post(url, json=data)
        res = response.json()['res']
        return res

if __name__ == "__main__":
    prompt_generation = Prompt_generation()
    private_models_url = models_url
    model = GPT2_model(prompt_generation, private_models_url, 'gpt2')
    result = model('今天天气如何')