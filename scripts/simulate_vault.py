from brownie import Vault, JTN, accounts
from web3 import Web3

initial_supply = 1000000

signer = accounts[2]
randomUser = accounts[3]

def deploy_token():
    token = JTN.deploy(initial_supply, {'from': signer})
    print("Token({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 
    
def deploy_vault(token):
    vault = Vault.deploy(token.address, {'from': signer})
    print("Vault is deployed at {0} successfully.".format(vault.address))
    return vault

def query(token,vault):
    a = vault.totalSupply()
    b = token.balanceOf(vault.address)
    result = "==" if a==b else "!="
    print("vault.totalSupply(shares) {1}{0}{2} token.balanceOf(vault)".format(result,a,b))
    # print("token.balanceOf(signer): ", token.balanceOf(signer))

def deposit(vault,amount=100):
    vault.deposit(amount,{'from': signer})
    
def withdraw(vault,share=100):
    vault.withdraw(share,{'from': signer})

def main():
    token = deploy_token()
    vault = deploy_vault(token)
    
    print("-----------APPROVE------------------")
    token.approve(vault.address,1000, {'from': signer})
           
    if 0 :
        print("-----------DEPOSIT------------------")
        for i in range(5):
            deposit(vault)
            query(token,vault)
            print("*******************************", i+1)
            
        print("---------WITHDRAW--------------------")
        for i in range(5):
            withdraw(vault)
            query(token,vault)
            print("*******************************", i+1)
            
    else:
        print("-----------signer2randomUser------------------")
        token.transfer(randomUser.address,10000, {'from': signer})
        print("-----------APPROVE------------------")
        token.approve(vault.address,1000, {'from': randomUser})    
        print("-----------randomUser2Vault------------------")
        token.transfer(vault.address,100, {'from': randomUser})
        
        print("-----------DEPOSIT------------------")
        amount = 100
        for i in range(5):
            oldTsupply = vault.totalSupply()
            deposit(vault,amount=amount)
            newTsupply = vault.totalSupply()
            print("amount(in): {0}, shares(out): {1}".format(amount,newTsupply - oldTsupply))
            assert (newTsupply - oldTsupply) <= amount
            assert  token.balanceOf(vault) >= newTsupply
            query(token,vault)
            print("*******************************", i+1)
            
        print("---------WITHDRAW--------------------")
        share = 100
        for i in range(5):
            oldBalance = token.balanceOf(vault)
            oldTsupply = vault.totalSupply()
            if oldTsupply == 0:
                break
            withdraw(vault,share=share)
            newBalance = token.balanceOf(vault)
            print("shares(in): {0}, amount(out): {1}".format(share,oldBalance-newBalance))
            assert  newBalance >= vault.totalSupply()
            query(token,vault)
            print("*******************************", i+1)        
    