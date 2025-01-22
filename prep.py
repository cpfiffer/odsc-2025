import outlines
from sentence_transformers import SentenceTransformer

# Load the embedding model
embedding_model = SentenceTransformer("mixedbread-ai/mxbai-embed-xsmall-v1")

model_string = 'Qwen/Qwen2.5-1.5B-Instruct'

print(f"Loading {model_string}")
llm = outlines.models.transformers(
    model_string,
)
print(f"Loaded {model_string}")
