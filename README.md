<div align="center">
    <h1 align="center">Serving SentenceTransformers with BentoML</h1>
</div>

[SentenceTransformers](https://www.sbert.net) is a Python framework for state-of-the-art sentence, text and image embeddings.

This is a BentoML example project, demonstrating how to build a sentence embedding inference API server, using a SentenceTransformers model [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). See [here](https://github.com/bentoml/BentoML?tab=readme-ov-file#%EF%B8%8F-what-you-can-build-with-bentoml) for a full list of BentoML example projects.

## Prerequisites

- You have installed Python 3.8+ and `pip`. See the [Python downloads page](https://www.python.org/downloads/) to learn more.
- You have a basic understanding of key concepts in BentoML, such as Services. We recommend you read [Quickstart](https://docs.bentoml.com/en/latest/get-started/quickstart.html) first.
- (Optional) We recommend you create a virtual environment for dependency isolation for this project. See the [Conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or the [Python documentation](https://docs.python.org/3/library/venv.html) for details.

## Install dependencies

```bash
git clone https://github.com/bentoml/BentoSentenceTransformers.git
cd BentoSentenceTransformers
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

For detailed explanations of the Service code, see [Sentence Transformer](https://docs.bentoml.org/en/latest/use-cases/embeddings/sentence-transformer.html).

## Deploy to BentoCloud

After the Service is ready, you can deploy the application to BentoCloud for better management and scalability. [Sign up](https://www.bentoml.com/) if you haven't got a BentoCloud account.

Make sure you have [logged in to BentoCloud](https://docs.bentoml.com/en/latest/bentocloud/how-tos/manage-access-token.html), then run the following command to deploy it.

```bash
bentoml deploy .
```

Once the application is up and running on BentoCloud, you can access it via the exposed URL.

**Note**: For custom deployment in your own infrastructure, use [BentoML to generate an OCI-compliant image](https://docs.bentoml.com/en/latest/guides/containerization.html).
