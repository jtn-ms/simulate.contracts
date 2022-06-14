from brownie import StakingToken, accounts
from web3 import Web3

initial_supply = 1000000

def main():
    account = accounts[0]
    st_token = StakingToken.deploy(initial_supply, {'from': account})
    print(st_token.name())
    
    
    