import bentoml

# Save model to BentoML local model store
if __name__ == "__main__":
    try:
        bentoml.models.get("all-MiniLM-L6-v2")
        print("Model already exists")
    except:
        import huggingface_hub
        with bentoml.models.create(
            "all-MiniLM-L6-v2",
        ) as model_ref:
            huggingface_hub.snapshot_download("sentence-transformers/all-MiniLM-L6-v2", local_dir=model_ref.path, local_dir_use_symlinks=False)
            print(f"Model saved: {model_ref}")
            