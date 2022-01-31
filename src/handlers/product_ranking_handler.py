from retrieval.emb_products_retrieval import EmbProductRetrieval
from utils.bert_utils import BertUtils

class ProductRankingHandler:
    NUM_PRODUCTS = 5

    @staticmethod
    def product_rec(user, message):
        # recommend some products matching user's message
        msg_keyword_emb = BertUtils.get_bert_emb_keyword(message)
        # retrieve
        emb_retrieval = EmbProductRetrieval(100)
        products = emb_retrieval.retrieve(user, msg_keyword_emb)

        # ranking

        return products[:ProductRankingHandler.NUM_PRODUCTS]