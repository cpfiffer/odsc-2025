# ODSC AI Builders Summit

This repository contains resources for my talk on applying structured language model outputs to RAG applications. We will use [Outlines](https://github.com/dottxt-ai/outlines) for structured output and [Milvus](https://milvus.io/) as a vector database.

The workshop is intended to be run entirely on your computer as a Jupyter Notebook. RAG and language models can both be computationally intensive, so the workshop is designed to be accessible to users with all levels of hardware.

Note that this means you will need to download model weights for both an embedding model and a language model.

__Download the model weights before the course!__ It will be hard to follow along if you are waiting for the model(s) to download.

## Setup

1. **Clone this repository**

```bash
git clone https://github.com/cpfiffer/odsc-2025.git
cd odsc-2025
```

2. **Install requirements**

You will need to install the following packages:

```bash
pip install "pymilvus[model]" "outlines[transformers]" datasets sentence-transformers scikit-learn matplotlib pandas einops sentencepiece
```

You may also install the package from the `requirements.txt` file in the repository:

```bash
pip install -r requirements.txt
```

3. **Download the models**

You will need to download the models in advance.

Please run the script `prep.py` to download

- The embedding model `mixedbread-ai/mxbai-embed-xsmall-v1`
- The language model `Qwen/Qwen2.5-1.5B-Instruct`
