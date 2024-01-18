class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self) -> None:
        self.__product_price = {}
        self.__product_quantity = {}
        self.__profite = 0
    
    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)

        self.__product_price[product.name] = product.price
        self.__product_quantity[product.name] = product.quantity
    
    def buy_product(self, name, quantity):
        if name in self.__product_price:
            if self.__product_quantity[name]>=quantity:
                self.__profite += ((5*self.__product_price[name])/100)*quantity
                self.__product_quantity[name]-=quantity
                print('Thank you')
            else:
                print('Unavailable')
        else:
            print('Not Found')

    def show_product(self):
        print("all products price:", self.__product_price)
        print("all products quantity:", self.__product_quantity)
    
    def show_profit(self):
        print("Profit: ", self.__profite)

class Shop(Store):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()

store = Shop('X-phone')
store.add_product('iphone', 100, 7)
store.add_product('samsung', 50, 7)

store.buy_product('iphone', 5)
store.show_product()
store.show_profit()
