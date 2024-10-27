from datetime import date
class Subscription:
    def __init__(self,expiration_date,is_paid=False):
        self.expiration_date = expiration_date
        self.is_paid = is_paid
    def __bool__(self):
        return self.is_paid and self.expiration_date > date.today()

subscription1 = Subscription(expiration_date=date(2024, 12, 31), is_paid=True)
subscription2 = Subscription(expiration_date=date(2023, 8, 15), is_paid=False)

if subscription1:
    print("Subscription is active.")  # Выводится
if subscription2:
    print("Subscription is active.")  # Не выводится