from brownie import JTN, accounts
from web3 import Web3

initial_supply = 1000000

def main():
    account = accounts[0]
    jtn_token = JTN.deploy(initial_supply, {'from': account})
    print(jtn_token.name())
    
    
    