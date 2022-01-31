import json
import os
from data.product_info import Product
from utils.bert_utils import BertUtils

class ProductLoader:
    PRODUCT_FILE = '/resources/product_data/products.json'
    products = []

    @staticmethod
    def load_products():
        #  "product_4": {"name":  "desk", "price": 20.0, "inventory":  200}
        with open(os.getcwd() + ProductLoader.PRODUCT_FILE) as sf:
            prod_data = json.load(sf)
            for pid, info in prod_data.items():
                prod_emb = BertUtils.get_bert_emb_keyword_sum(info['name'])
                ProductLoader.products.append(Product(product_id=pid,
                                                      product_name=info['name'],
                                                      price=info['price'],
                                                      emb=prod_emb))




