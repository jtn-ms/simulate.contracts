from unicodedata import decimal
from brownie import TetherToken, accounts
from web3 import Web3

initial_supply = 1000000
name = "USDT"
symbols = "USDT"
decimals = 10**18


def main():
    account = accounts[0]
    usdt_token = TetherToken.deploy(initial_supply, name, symbols, decimals, {'from': account})
    print(usdt_token.name())
    