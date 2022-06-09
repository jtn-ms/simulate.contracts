# [Share Section]
# uint public totalSupply;
# mapping(address => uint) public balanceOf;
# _mint()
# _burn() 
#
# [Liquidity Section]
# token = IERC20(_token);
#
# [BASE EQUATION]
# shares/totalSupply == amount_in/token.balanceOf(address(this))
# if token.balanceOf(address(vault)) == vault.totalSupply
# shares == amount
# 
# [deposit]
# shares = (amount_in * totalSupply) / token.balanceOf(address(this));
# [withdraw]
# amount = (shares_out * token.balanceOf(address(this))) / totalSupply;
#
#

from brownie import Vault, MyToken, accounts
from web3 import Web3

initial_supply = 1000000

signer = accounts[2]

def deploy_token():
    token = MyToken.deploy(initial_supply, {'from': signer})
    print(token.name())
    return token 
    
def deploy_vault(token_address):
    vault = Vault.deploy(token_address, {'from': signer})
    print(vault.token())
    return vault

def query(token,vault):
    print("vault.totalSupply: ",vault.totalSupply())
    print("token.balanceOf(vault): ", token.balanceOf(vault.address))   
    print("token.balanceOf(signer): ", token.balanceOf(signer))

def deposit(vault,amount=100):
    vault.deposit(amount,{'from': signer})
    
def withdraw(vault,share=100):
    vault.withdraw(share,{'from': signer})

def main():
    token = deploy_token()
    vault = deploy_vault(token.address)
    print("------------------------------")
    print(token.address)
    print(token.name())
    print(vault.address)
    print(vault.token())
    print("-----------APPROVE------------------")
    token.approve(vault.address,1000, {'from': signer})
    print("-----------DEPOSIT------------------")
    for i in range(5):
        deposit(vault)
        query(token,vault)
        print("*******************************")
    print("---------WITHDRAW--------------------")
    for i in range(5):
        withdraw(vault)
        query(token,vault)
        print("*******************************")
    