import uvicorn
from fastapi import FastAPI, Response, Header, Request
from model_libs.model_loader import ModelLoader
from data.product_loader import ProductLoader
from data.review_info import ReviewProcess
from model_libs.intent_rule_loader import IntentRule
from utils.logging_utils import Logger
from utils.bert_utils import BertUtils
from handlers.product_ranking_handler import ProductRankingHandler
from handlers.place_order_handler import PlaceOrderHandler

app = FastAPI()

@app.on_event("startup")
async def startup():
    Logger.init_logger()
    Logger.logger.info("logger initialized")
    BertUtils.load_bert_model()
    Logger.logger.info("bert model loaded")
    ModelLoader.init_models_map()
    Logger.logger.info("ranking model loaded")
    ProductLoader.load_products()
    Logger.logger.info("products loaded")
    ReviewProcess.load_review_data()
    Logger.logger.info("review loaded")

    Logger.logger.info("server started up")

@app.get('/')
async def index():
    return 'chat bot server'

@app.get('/place_order/')
async def chat_ai(user: str, product_id: str, shop_id: str):
    PlaceOrderHandler.handle_place_order(user, product_id, shop_id)

@app.get('/submit_review/')
async def sub_review(user: str, product_id: str, review: str, rating: int):
    ReviewProcess.write_review(product_id, user, review, rating)

@app.get('/message/')
async def chat_ai(user: str, message: str):
    print(user, message)

    intent = IntentRule.get_intent(message)
    if intent is None:
        return None

    rule_response = IntentRule.get_response(intent)
    if rule_response is not None:
        return rule_response

    if intent == IntentRule.PROD_REC:
        return ProductRankingHandler.product_rec(user, message)
    elif intent == IntentRule.RETURN_ORDER:
        return PlaceOrderHandler.handle_place_order(user, message)
    return None

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=80)
