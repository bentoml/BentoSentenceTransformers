<div align="center">
    <h1 align="center">Serving SentenceTransformers with BentoML</h1>
</div>

[SentenceTransformers](https://www.sbert.net) is a Python framework for state-of-the-art sentence, text and image embeddings.

This is a BentoML example project, demonstrating how to build a sentence embedding inference API server, using a SentenceTransformers model [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2).

## Install dependencies

```bash
git clone https://github.com/bentoml/BentoSentenceTransformers.git
cd BentoSentenceTransformers

# Recommend Python 3.11
pip install -r requirements.txt
```

## Run the BentoML Service

We have defined a BentoML Service in `service.py`. Run `bentoml serve` in your project directory to start the Service.

```bash
$ bentoml serve .

2024-01-18T06:40:53+0800 [INFO] [cli] Prometheus metrics for HTTP BentoServer from "service:SentenceEmbedding" can be accessed at http://localhost:3000/metrics.
2024-01-18T06:40:54+0800 [INFO] [cli] Starting production HTTP BentoServer from "service:SentenceEmbedding" listening on http://localhost:3000 (Press CTRL+C to quit)
Model loaded device: cpu
```

The server is now active at [http://localhost:3000](http://localhost:3000/). You can interact with it using the Swagger UI or in other different ways.

CURL

```bash
curl -X 'POST' \
  'http://localhost:3000/encode' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sentences": [
    "hello world"
  ]
}'
```

Python client

```python
import bentoml

with bentoml.SyncHTTPClient("http://localhost:3000") as client:
    result = client.encode(
        sentences=[
                "hello world"
        ],
    )
```

For custom deployment in your own infrastructure, use [BentoML to generate an OCI-compliant image](https://docs.bentoml.com/en/latest/guides/containerization.html).
