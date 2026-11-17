
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import numpy as np

# 1. Connect to Gemini
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# 2. Create 10 sentences
sentences = [
    "I love learning Python programming.",
    "Python is a great language for coding.",
    "I enjoy developing software applications.",
    "Machine learning helps computers learn from data.",
    "Artificial intelligence is transforming technology.",
    "I want to become a software engineer.",
    "The weather is very cold today.",
    "I like playing cricket with my friends.",
    "Deep learning is a part of machine learning.",
    "I enjoy writing Python code every day."
]

# 3. Generate embeddings
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=sentences,
    config=types.EmbedContentConfig(
        task_type="SEMANTIC_SIMILARITY"
    )
)

embeddings = [
    item.values for item in response.embeddings
]

print("Total sentences:", len(sentences))
print("Total embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))

# 4. Calculate cosine similarity
def cosine_similarity(vector1, vector2):

    dot_product = np.dot(vector1, vector2)

    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)

    return dot_product / (norm1 * norm2)


# 5. Compare all sentence pairs
similarities = []

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):

        score = cosine_similarity(
            embeddings[i],
            embeddings[j]
        )

        similarities.append(
            (sentences[i], sentences[j], score)
        )

# 6. Sort by similarity score
similarities.sort(
    key=lambda x: x[2],
    reverse=True
)

# 7. Display top 10 matches
print("\nMOST SIMILAR SENTENCES\n")

for sentence1, sentence2, score in similarities[:10]:

    print("Sentence 1:", sentence1)
    print("Sentence 2:", sentence2)
    print("Similarity:", round(float(score), 4))
    print("-" * 60)
