from models.product import Product


class ProductService:

    @staticmethod
    def get_all_products():

        return Product.query.all()

    @staticmethod
    def get_product(product_id):

        return Product.query.get(product_id)
