import gc


# Category
class Category:
    id = 0

    def add_id(self):
        Category.id += 1
        return Category.id

    def __init__(self, id, name):
        self.id = self.add_id()
        self.name = name

    def get_name(self):
        return self.name


# Product
class Product:
    id = 0

    def add_id(self):
        Category.id += 1
        return Category.id

    def __init__(self, id, name, category, price):
        self.id = self.add_id()
        self.name = name
        self.category: Category
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_searcher(self):
        return f'Siz qidirgan tovarlar nomi = {self.name}, narxi = {self.price}.'

    def do_nasiya(self, long):
        if long == 3:
            nasiya_price = self.price * 0.1 + self.price
            return f'{long} oyga {nasiya_price // long} sumdan tulang.Jami({nasiya_price})'
        if long == 6:
            nasiya_price = self.price * 0.15 + self.price
            return f'{long} oyga {nasiya_price // long} sumdan tulang.Jami({nasiya_price})'
        if long == 12:
            nasiya_price = self.price * 0.3 + self.price
            return f'{long} oyga {nasiya_price // long} sumdan tulang.Jami({nasiya_price})'

    def __repr__(self):
        return f'{self.name}'


# Basket
class Basket:
    def __init__(self):
        self.basket_list = []
        self.basket_dict = {}

    def add_product(self, product, quantity):
        self.basket_list.extend([product for _ in range(quantity)])

    def get_products(self):
        return self.basket_list

    def get_total_products(self):
        return len(set(self.basket_list))

    def get_all_price(self):
        return sum([product.price for product in self.get_products()])


# Search
class Search:
    def __init__(self, name: str):
        self.name = name
        self.search_prod = []

    def search_product(self):
        # for obj in gc.get_objects():
        #     if isinstance(obj, Product) and obj.name == self.name:
        #         print(obj.get_searcher())
        return [obj.get_searcher() for obj in gc.get_objects() if isinstance(obj, Product) and obj.name == self.name]


books = Category(1, "Kitoblar")
fruits = Category(2, "Mevalar")

book_1 = Product(1, "Kitob 1", books, 89000)
book_5 = Product(5, "Kitob 1", books, 99000)
book_2 = Product(2, "Kitob 2", books, 58000)
book_3 = Product(3, "Kitob 3", books, 10540)
book_4 = Product(4, "Kitob 4", books, 78504)

meva_1 = Product(1, "meva 1", fruits, 89000)
meva_2 = Product(2, "meva 2", fruits, 58000)
meva_3 = Product(3, "meva 3", fruits, 10540)
meva_4 = Product(4, "meva 4", fruits, 78504)
# print(book_1.do_nasiya(12))
basket1 = Basket()
basket1.add_product(book_1, 1)
basket1.add_product(book_2, 2)
basket1.add_product(book_3, 3)
basket1.add_product(book_4, 4)
# print(basket1.get_products())
# print(basket1.get_total_products())
# print(basket1.get_all_price())
search_word = input("Qidirmoqchi bulgan kitobingizni nomini kiriting: ")
ser_k = Search(search_word)
print(ser_k.search_product())
