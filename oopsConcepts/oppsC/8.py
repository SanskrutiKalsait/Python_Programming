#.Create a class method to change the bank name.

class Bank:
    bank_name = "State Bank of India"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

Bank.change_bank_name("HDFC Bank")

print("Bank Name:", Bank.bank_name)


