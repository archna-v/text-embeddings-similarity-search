# Text Embeddings and Similarity Search

## About the Project

This project explores how text can be converted into numerical representations called **embeddings** and how these embeddings can be used to identify semantically similar sentences.

Using the Gemini Embedding API and Python, this project generates embeddings for 10 sentences and calculates cosine similarity to find the most similar sentence pairs.

## Objectives

- Understand text embeddings and vector representations.
- Convert text into numerical vectors using Gemini.
- Understand semantic similarity.
- Calculate cosine similarity using NumPy.
- Perform similarity search on a collection of sentences.

## Technologies Used

- Python
- Google Gemini Embedding API
- NumPy
- Google Gen AI SDK
- python-dotenv

## Project Structure

```text
text-embeddings-similarity-search/
│
├── embeddings.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Key Concepts

| Concept | Description |
|---|---|
| Embeddings | Numerical representations of text |
| Vectors | Ordered lists of numbers |
| Semantic Similarity | Similarity based on meaning |
| Cosine Similarity | Measures similarity between two vectors |
| Similarity Search | Finds the most similar vectors |

## How It Works

1. Create a collection of 10 sentences.
2. Generate embeddings for each sentence using the Gemini Embedding API.
3. Extract the numerical vectors.
4. Calculate cosine similarity between sentence pairs using NumPy.
5. Sort the similarity scores in descending order.
6. Display the 10 most similar sentence pairs.

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/archna-v/text-embeddings-similarity-search.git
cd text-embeddings-similarity-search
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment (Windows)**

```bash
venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Configure your API key**

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Gemini API key.

**6. Run the project**

```bash
python embeddings.py
```

## Expected Output

- Total sentences: 10
- Total embeddings: 10
- Embedding dimensions: 3072 (default model output)
- Top 10 most semantically similar sentence pairs with their cosine similarity scores.

*Note: Similarity scores depend on the embedding model and input sentences.*

## Learning Outcome

Through this project, I gained practical experience in generating text embeddings, understanding semantic similarity, calculating cosine similarity, and implementing a basic similarity search system.

These concepts form an important foundation for building Retrieval-Augmented Generation (RAG) applications.

---

**Part of my LLM and Generative AI learning journey.**
