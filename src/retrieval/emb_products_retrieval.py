from data.product_loader import ProductLoader
from utils.bert_utils import BertUtils

class EmbProductRetrieval:

    def __init__(self, k):
        self._num_products = k

    def retrieve(self, user_id, msg_keyword_emb):

        product_res = []
        for product in ProductLoader.products:
            max_score = 0.0
            for emb_keyword in msg_keyword_emb:
                score = BertUtils.cosine_score(emb_keyword, product.emb)
                if score > max_score:
                    max_score = score
            product_res.append({'product_id': product.product_id, 'name': product.product_name, 'score': max_score})

        product_res.sort(key=lambda k: k['score'], reverse=True)


        return product_res[:self._num_products]