from brownie import WETH9, accounts
from web3 import Web3

initial_supply = 1000000

def main():
    account = accounts[0]
    weth_token = WETH9.deploy({'from': account})
    print(weth_token.name())
    