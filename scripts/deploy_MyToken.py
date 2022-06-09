from brownie import MyToken, accounts
from web3 import Web3

initial_supply = 1000000

def main():
    account = accounts[0]
    my_token = MyToken.deploy(initial_supply, {'from': account})
    print(my_token.name())
    
    
    