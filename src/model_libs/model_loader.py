from model_libs.dummy_model import DummyModel

class ModelLoader:
    model_map = None

    @staticmethod
    def load():
        return

    @staticmethod
    def init_models_map():
        ModelLoader.model_map = {'dummy': DummyModel()}