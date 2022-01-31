import random

from model_libs.base_model import BaseModel

class DummyModel(BaseModel):

    def predict(self, features):
        return random.random()