class WarehouseItem:
    def __init__(self,quantity,is_reserved=False):
        self.quantity = quantity
        self.is_reserved = is_reserved
    def __bool__(self):
        return self.quantity > 0 and not self.is_reserved
    
item1 = WarehouseItem(quantity=10, is_reserved=False)
item2 = WarehouseItem(quantity=0, is_reserved=True)
item3 = WarehouseItem(quantity=5, is_reserved=True)

if item1:
    print("1Item is available for sale.")  # Выводится
if item2:
    print("2Item is available for sale.")  # Не выводится
if item3:
    print("3Item is available for sale.")  # Не выводится
