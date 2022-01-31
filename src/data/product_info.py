from dataclasses import dataclass

@dataclass
class Product:
    product_id: str
    product_name: str
    price: float
    emb: list