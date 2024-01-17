import numpy as np
import torch
import bentoml
from sentence_transformers import SentenceTransformer, models

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"

@bentoml.service(
    traffic={"timeout": 60},
    resources={"memory": "2Gi"},
)
class SentenceEmbedding:

    def __init__(self) -> None:
        
        # Load model and tokenizer
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # define layers
        first_layer = SentenceTransformer(MODEL_ID)
        pooling_model = models.Pooling(first_layer.get_sentence_embedding_dimension())
        self.model = SentenceTransformer(modules=[first_layer, pooling_model])
        print("Model loaded", "device:", self.device)


    @bentoml.api(batchable=True)
    def encode(
        self,
        sentences: list[str],
    ) -> np.ndarray:
        # Tokenize sentences
        sentence_embeddings= self.model.encode(sentences)
        return sentence_embeddings

if __name__ == "__main__":
    SentenceEmbedding.serve_http()
    