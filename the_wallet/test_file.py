# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

import pytest

# === CODE ===

class InsufficientAmount(Exception):
    pass


class Wallet:

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

# === TESTS ===

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


def test_setting_initial_amount():
    wallet = Wallet(20)
    assert wallet.balance == 20


def test_wallet_add_cash():
    wallet = Wallet(20)
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
