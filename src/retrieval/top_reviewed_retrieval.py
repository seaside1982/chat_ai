from data.review_info import ReviewProcess

class TopReviewedRetrieval:
    def __init__(self):
        return

    def retrieve(self, topk):
        return [k['product_id'] for k in ReviewProcess.agg_review_data[:topk]]