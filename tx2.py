class ShoppingCart:
    def __init__(self,items:list):
        self.items = items
    @property
    def total_price(self):
        return self.items
    @total_price.setter
    def total_price(self, value):
        self.items = value
    def __bool__(self):
       return True if self.items else False
   

cart1 = ShoppingCart(items=["laptop", "phone"])
cart2 = ShoppingCart(items=[])

if cart1:
    print("Cart1 has items.")  # Выводится
if cart2:
    print("Cart2 has items.")  # Не выводится
