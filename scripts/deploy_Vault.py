from brownie import Vault,MyToken, accounts
from web3 import Web3

MyTokenAddress = "0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87"

def main():
    account = accounts[0]
    vault = Vault.deploy(MyTokenAddress, {'from': account})
    print(vault.token())
    