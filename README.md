# -17.-Magic-__bool__-method-of-determining-object-truthfulness-Python-OOP

Description
This repository contains a collection of Python classes designed to demonstrate the functionality of custom __bool__ methods, allowing for more intuitive conditional evaluations in various object contexts. Each class serves a specific purpose, from representing shopping carts to managing subscriptions and warehouse items, making it easy to understand Python's __bool__ method in practical scenarios.

# Bool-Driven-Classes

This repository contains Python classes showcasing the use of custom `__bool__` methods to simplify object conditionals. The classes provide real-world examples where objects are evaluated as `True` or `False` based on their attributes, offering a clean and Pythonic approach to conditional logic.

## Classes Overview

1. **ShoppingCart**
    - **File**: `tx2.py`
    - **Description**: Represents a shopping cart with items. The cart is considered `True` (i.e., non-empty) if it contains any items.
    - **Usage**:
      ```python
      cart1 = ShoppingCart(items=["laptop", "phone"])
      cart2 = ShoppingCart(items=[])
      
      if cart1:
          print("Cart1 has items.")  # Prints
      if cart2:
          print("Cart2 has items.")  # Does not print
      ```

2. **Subscription**
    - **File**: `tx4.py`
    - **Description**: Represents a user subscription with an expiration date. The subscription is considered `True` (active) if it’s paid and has not expired.
    - **Usage**:
      ```python
      subscription1 = Subscription(expiration_date=date(2024, 12, 31), is_paid=True)
      subscription2 = Subscription(expiration_date=date(2023, 8, 15), is_paid=False)
      
      if subscription1:
          print("Subscription is active.")  # Prints
      if subscription2:
          print("Subscription is active.")  # Does not print
      ```

3. **WarehouseItem**
    - **File**: `tx5.py`
    - **Description**: Represents an item in a warehouse. The item is `True` (available for sale) if the quantity is greater than zero and it is not reserved.
    - **Usage**:
      ```python
      item1 = WarehouseItem(quantity=10, is_reserved=False)
      item2 = WarehouseItem(quantity=0, is_reserved=True)
      item3 = WarehouseItem(quantity=5, is_reserved=True)
      
      if item1:
          print("Item1 is available for sale.")  # Prints
      if item2:
          print("Item2 is available for sale.")  # Does not print
      if item3:
          print("Item3 is available for sale.")  # Does not print
      ```

## How to Run
To test each class, simply run the respective Python file. Each file includes sample objects and conditionals to demonstrate the functionality.

## Requirements
- Python 3.x
- `datetime` module (built-in)

## License
This project is open-source and available under the MIT License.

---

Enjoy exploring the use of custom `__bool__` methods to make your Python objects more intuitive in conditional expressions!
