import unittest
from data.product_loader import ProductLoader
from data.review_info import ReviewProcess
from handlers.product_ranking_handler import ProductRankingHandler
from retrieval.top_reviewed_retrieval import TopReviewedRetrieval
from model_libs.model_loader import ModelLoader
from model_libs.intent_rule_loader import IntentRule
from utils.bert_utils import BertUtils

class TestRankingServer(unittest.TestCase):
    def test_top_reviewed(self):
        ReviewProcess.load_review_data()
        rt = TopReviewedRetrieval()
        top_review_r = rt.retrieve(topk=1)

        self.assertEqual(top_review_r[0], 'product_2')

    def test_product_ranking(self):
        BertUtils.load_bert_model()
        ProductLoader.load_products()
        rec_res = ProductRankingHandler.product_rec("user_1", "show me some shoe")
        self.assertEqual(rec_res[0]['name'], "shoe")

    def test_intent_parse(self):
        BertUtils.load_bert_model()
        IntentRule.init_rule()
        intent = IntentRule.get_intent("how are you")
        self.assertEqual(intent, "greeting")
        resp = IntentRule.get_response(intent)
        self.assertTrue(resp, IntentRule.intent2response[intent])

    def test_overral(self):
        # initialization
        ModelLoader.init_models_map()

        model_type = "dummy"
        model = ModelLoader.model_map[model_type]

        score = model.predict(features=[])
        self.assertTrue(score > 0.0 and score < 1.0)

if __name__ == '__main__':
    unittest.main()
