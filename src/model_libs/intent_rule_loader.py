from scipy.spatial.distance import cosine
from utils.bert_utils import BertUtils
import json
import numpy as np
import os

class IntentRule:
    intent2embedding = {}
    intent2response = {}
    intent_threshold = 0.5

    INTENT_SENTENCE_FILE = '/resources/rule_data/intent_sentences.json'
    INTENT_RESPONSE_FILE = '/resources/rule_data/intent_response.json'

    PROD_REC = "product_recommendation"
    RETURN_ORDER = "return_order"

    @staticmethod
    def init_rule():
        with open(os.getcwd() + IntentRule.INTENT_SENTENCE_FILE) as sf:
            intent2sentences = json.load(sf)
        for intent, sentences in intent2sentences.items():
            s_emb = BertUtils.get_bert_embs(sentences)
            IntentRule.intent2embedding[intent] = np.sum(s_emb, axis=0)
        with open(os.getcwd() + IntentRule.INTENT_RESPONSE_FILE) as sf:
            IntentRule.intent2response = json.load(sf)

    @staticmethod
    def get_intent(msg):
        msg_embedding = BertUtils.get_bert_emb_keyword_sum(msg)

        max_intent_score, most_likely_intent = 0.0, None
        for intent, intent_emb in IntentRule.intent2embedding.items():
            score = BertUtils.cosine_score(msg_embedding, intent_emb)
            if score > max_intent_score:
                max_intent_score = score
                most_likely_intent = intent
        if max_intent_score > IntentRule.intent_threshold:
            return most_likely_intent
        return None

    @staticmethod
    def get_response(intent):
        if intent in IntentRule.intent2response:
            return IntentRule.intent2response[intent]
        return None






