import numpy as np
import torch
import bentoml
from sentence_transformers import SentenceTransformer, models


@bentoml.service(traffic={"timeout": 1})
class SentenceEmbedding:
    model_ref = bentoml.models.get("all-MiniLM-L6-v2")

    def __init__(self) -> None:
        
        # Load model and tokenizer
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # define layers
        first_layer = SentenceTransformer(self.model_ref.path)
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
    