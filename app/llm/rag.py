from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_knowledge_base(texts):
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, texts

def ask_question(question, index, texts):
    q_vector = model.encode([question])
    distances, indices = index.search(np.array(q_vector), k=1)
    return texts[indices[0][0]]

if __name__ == '__main__':
    docs = ['Q1 revenue was 500000 rupees.','North region had 40 percent of sales.','Laptop generated highest revenue.','Best salesperson was Rahul with 80000 sales.','Q2 target is 600000.']
    index, texts = build_knowledge_base(docs)
    print('Knowledge base ready!')
    for q in ['What was Q1 revenue?','Which region is best?','Who is best salesperson?']:
        print(f'Q: {q}')
        print(f'A: {ask_question(q, index, texts)}')
        print()
