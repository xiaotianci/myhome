from dataclasses import dataclass, asdict

@dataclass
class Models_url:
    gpt2_url : str = "http://127.0.0.1:9363/infer"
    qwen2d5_1d5b : str = "http://127.0.0.1:9363/infer"


models_url = asdict(Models_url())