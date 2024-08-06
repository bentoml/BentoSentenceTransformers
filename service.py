from __future__ import annotations

import typing as t

import numpy as np
import bentoml


SAMPLE_SENTENCES = [
    "The sun dips below the horizon, painting the sky orange.",
    "A gentle breeze whispers through the autumn leaves.",
    "The moon casts a silver glow on the tranquil lake.",
    "A solitary lighthouse stands guard on the rocky shore.",
]

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"

@bentoml.service(
    traffic={"timeout": 60},
    resources={"gpu": "nvidia-t4"},
)
class SentenceTransformers:

    def __init__(self) -> None:
        import torch
        from sentence_transformers import SentenceTransformer, models
        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(MODEL_ID, device=self.device)
        print(f"Model '{MODEL_ID}' loaded on device: '{self.device}'.")

    @bentoml.api(batchable=True)
    def encode(
        self,
        sentences: t.List[str] = SAMPLE_SENTENCES,
    ) -> np.ndarray:
        return self.model.encode(sentences)
