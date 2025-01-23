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

You must install the package from the `requirements.txt` file in the repository:

```bash
pip install -r requirements.txt
```

You can also install the packages directly with pip, though the `requirements.txt` install method is recommended.

```bash
pip install "pymilvus[model]" "outlines[transformers]" datasets sentence-transformers scikit-learn matplotlib pandas einops jupyterlab sentencepiece
```


3. **Download the models**

You will need to download the models in advance.

Please run the script `prep.py` to download

- The embedding model `mixedbread-ai/mxbai-embed-xsmall-v1`
- The language model `Qwen/Qwen2.5-1.5B-Instruct`

4. **Start Jupyter**

As this is a notebook, you will need some form of Jupyter notebook viewer. The `requirements.txt` file will install Jupyter Lab by default.

To run Jupyter Lab, run

```bash
jupyter lab
```

and open the `lesson.ipynb` notebook.
