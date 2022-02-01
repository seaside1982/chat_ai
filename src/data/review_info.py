from dataclasses import dataclass
import json, os

@dataclass
class ReviewData:
    product_id: str
    user_id: str
    review_text: str
    rating: int

class ReviewProcess:
    REVIEW_FILE = "/resources/product_data/review_data.json"
    review_data: list = []
    agg_review_data: list = []

    @staticmethod
    def write_review(self, product_id, user, review, rating):
        ReviewProcess.review_data.append(ReviewData(product_id, user, review, rating))

    @staticmethod
    def load_review_data():
        with open(os.getcwd() + ReviewProcess.REVIEW_FILE) as sf:
            ReviewProcess.agg_review_data = json.load(sf)

        ReviewProcess.agg_review_data.sort(key=lambda k: k['review_score'], reverse=True)

