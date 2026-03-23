class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        """Lấy số tài khoản (chỉ đọc)"""
        return self._account_number
    def deposit(self, amount):
        """Nạp tiền vào tài khoản"""
        if amount > 0:
            self._balance += amount
            print(f" Nạp thành công {amount}. Số dư: {self._balance}")
        else:
            print(" Số tiền nạp phải lớn hơn 0")
    def withdraw(self, amount):
        """Rút tiền từ tài khoản"""
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            print(f" Rút thành công {amount}. Số dư: {self._balance}")
        else:
            print(" Số dư không đủ để rút tiền")
    def get_balance(self):
        """Lấy số dư tài khoản"""
        return self._balance
    def display_account_info(self):
        """Hiển thị thông tin tài khoản"""
        print(f"Số tài khoản: {self.account_number}, Số dư: {self._balance}")


if __name__ == "__main__":
    account = BankAccount("123456789", balance=1000)
    account.display_account_info()
    print("Số dư hiện tại:", account.get_balance())
    account.deposit(500)
    print("Số dư sau khi nạp tiền:", account.get_balance())
    account.withdraw(200)
    print("Số dư sau khi rút tiền:", account.get_balance())
    account.withdraw(1500)
    print("Số dư sau khi rút tiền:", account.get_balance())
