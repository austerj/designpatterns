from abc import ABC, abstractmethod


class BankService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type):
        if account_type == 'debit':
            new_account = DebitAccount()
        elif account_type == 'credit':
            new_account = CreditAccount()
        else:
            raise ValueError('invalid account type')
        print(f'creating {account_type} account {new_account.number}')
        self.accounts[new_account.number] = new_account
        return new_account.number

    def _get_account(self, account_number):
        if account_number in self.accounts.keys():
            return self.accounts[account_number]
        else:
            raise ValueError('account number does not exist')

    def deposit(self, account_number, amount):
        self._get_account(account_number).deposit(amount)

    def withdraw(self, account_number, amount):
        self._get_account(account_number).withdraw(amount)


class Account(ABC):
    def __init__(self):
        self.number = self.__hash__()
        self.balance = 0

    def deposit(self, amount):
        self._check_positive_amount(amount)
        self._check_deposit_amount(amount)
        self.balance += amount
        print(f'{self.number}: deposited {amount}, balance is {self.balance}')

    def withdraw(self, amount):
        self._check_positive_amount(amount)
        self._check_withdrawal_amount(amount)
        self.balance -= amount
        print(f'{self.number}: withdrew {amount}, balance is {self.balance}')

    @staticmethod
    def _check_positive_amount(amount):
        if amount < 0:
            raise ValueError('amount must be positive')

    def _check_deposit_amount(self, amount):
        pass

    @abstractmethod
    def _check_withdrawal_amount(self, amount):
        raise NotImplementedError


class DebitAccount(Account):
    def _check_withdrawal_amount(self, amount):
        if self.balance < amount:
            raise ValueError('cannot withdraw amount, balance too small')


class CreditAccount(Account):
    def __init__(self, limit=2000):
        super().__init__()
        self.limit = limit

    def _check_withdrawal_amount(self, amount):
        if self.balance + self.limit < amount:
            raise ValueError('cannot withdraw amount, credit limit too small')


class Customer:
    def __init__(self):
        self.bankservice = BankService()
        self.debit = self.bankservice.create_account('debit')
        self.credit = self.bankservice.create_account('credit')


if __name__ == '__main__':
    # create a customer
    customer = Customer()
    # create accounts
    debit_account = customer.bankservice.create_account('debit')
    credit_account = customer.bankservice.create_account('credit')
    # deposit and withdraw using bankservice
    customer.bankservice.deposit(debit_account, 50)
    customer.bankservice.withdraw(credit_account, 2000)
    # overdraw credit account
    customer.bankservice.withdraw(credit_account, 100)
