class BankAccount:
    def __init__(self, balance, is_active=False):
        self.balance = balance
        self.is_active = is_active

    def validate_balance(self,value):
        if not isinstance(value, (float, int)):
            raise ValueError("Balance must be a number")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.validate_balance(value)
        self.__balance = value

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value):
        if not isinstance(value, bool):
            raise ValueError("Is active must be a boolean")
        self.__is_active = value

    def __bool__(self):
        return self.is_active and self.balance > 0
account1 = BankAccount(balance=1000, is_active=True)
account2 = BankAccount(balance=0, is_active=True)
account3 = BankAccount(balance=500, is_active=False)

if account1:
    print("Account is valid and has funds.")  # Выводится
if account2:
    print("Account is valid and has funds.")  # Не выводится
if account3:
    print("Account is valid and has funds.")  # Не выводится
