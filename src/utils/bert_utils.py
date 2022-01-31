from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import numpy as np

class BertUtils:
    bert_embedding = None

    @staticmethod
    def load_bert_model():
        BertUtils.bert_embedding = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    @staticmethod
    def get_bert_emb_keyword_sum(msg):
        return BertUtils.bert_embedding.encode([msg])[0]

    @staticmethod
    def get_bert_emb_keyword(msg):
        return BertUtils.bert_embedding.encode(msg.split(" "))

    @staticmethod
    def get_bert_embs(sentences):
        return BertUtils.bert_embedding.encode(sentences)

    @staticmethod
    def cosine_score(emb1, emb2):
        return 1 - cosine(emb1, emb2)


