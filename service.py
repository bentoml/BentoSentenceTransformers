import numpy as np
from bentoml import service, api
from bentoml.images import PythonImage as Image
from bentoml.models import HuggingFaceModel


SAMPLE_SENTENCES = [
    "The sun dips below the horizon, painting the sky orange.",
    "A gentle breeze whispers through the autumn leaves.",
    "The moon casts a silver glow on the tranquil lake.",
    "A solitary lighthouse stands guard on the rocky shore.",
]

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"


@service(
    image=Image(python_version="3.11").requirements_file("./requirements.txt"),
    resources={"gpu": 1, "gpu_type": "nvidia-t4"},
    envs=[{"name": "NORMALIZE", "value": "True"}],
)
class SentenceTransformers:
    model_path = HuggingFaceModel(MODEL_ID)

    def __init__(self) -> None:
        import torch
        from sentence_transformers import SentenceTransformer
        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(self.model_path, device=self.device)

    @api(batchable=True)
    def encode(
        self,
        sentences: list[str] = SAMPLE_SENTENCES,
    ) -> np.ndarray:
        return self.model.encode(sentences)
