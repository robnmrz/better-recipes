# here is where the magic happens
# from transformers import AutoModel, AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
# model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

ingredients = ["milk", "butter", "flour", "eggs", "sugar", "soda", "salt", "steak"]
categories = ["dairy", "baking", "meat", "minerals", "beverages", "custom"]

model = SentenceTransformer("all-MiniLM-L6-v2")

ingredient_vecs = model.encode(ingredients)
category_vecs = model.encode(categories)

for ingredient in ingredients:
    ingredient_vec = model.encode([ingredient])
    category_idx = cosine_similarity([ingredient_vec[0]], category_vecs).argmax()
    print(ingredient, categories[category_idx])
