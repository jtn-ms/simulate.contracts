import pytest
from brownie import Vault, JTN
from brownie import accounts
from web3 import Web3

@pytest.fixture(scope="module")
def initial_supply():
    return 1000000

@pytest.fixture(scope="module")
def signer():
    return accounts[0]

@pytest.fixture(scope="module")
def randomUser():
    return accounts[1]

# deploy token
@pytest.fixture(scope="module")
def token(initial_supply,signer):
    token = JTN.deploy(initial_supply, {'from': signer})
    return token 

@pytest.fixture(scope="module")    
def vault(token,signer):
    vault = Vault.deploy(token.address, {'from': signer})
    return vault

# shares <= amount
# shares == amount with only Direct Deposit
def test_onlyDirectDeposit(token,vault,signer):

    def deposit(vault,amount=100):
        vault.deposit(amount,{'from': signer})
        
    def withdraw(vault,share=100):
        vault.withdraw(share,{'from': signer})

    #################################################
    #### shares == amount without indirect deposit ##
    #################################################
    print("-----------APPROVE------------------")
    token.approve(vault.address,1000, {'from': signer})
    
    print("-----------DEPOSIT------------------")
    amount = 100
    for i in range(5):
        deposit(vault,amount=amount)
        assert  token.balanceOf(vault) == vault.totalSupply()
        
    print("---------WITHDRAW--------------------")
    share = 100
    for i in range(4):
        withdraw(vault,share=share)
        assert  token.balanceOf(vault) == vault.totalSupply()
 
 # amount == shares with inDirect Deposit       
def test_withIndrectDeposit(token,vault,signer,randomUser):
    def deposit(vault,amount=100):
        vault.deposit(amount,{'from': signer})
        
    def withdraw(vault,share=100):
        vault.withdraw(share,{'from': signer})
    ###############################################
    #### amount > share with indirect deposit #####
    ###############################################
    print("-----------signer2randomUser------------------")
    token.transfer(randomUser.address,10000, {'from': signer})
    print("-----------APPROVE------------------")
    token.approve(vault.address,1000, {'from': randomUser})    
    print("-----------randomUser2Vault------------------")
    token.transfer(vault.address,10000, {'from': randomUser})
    print("-----------DEPOSIT------------------")
    amount = 100
    for i in range(5):
        oldTsupply = vault.totalSupply()
        deposit(vault,amount=amount)
        newTsupply = vault.totalSupply()
        assert (newTsupply - oldTsupply) < amount
        assert  token.balanceOf(vault) >= newTsupply
        
    print("---------WITHDRAW--------------------")
    share = 100
    for i in range(5):
        oldBalance = token.balanceOf(vault)
        oldTsupply = vault.totalSupply()
        if oldTsupply == 0:
            break
        withdraw(vault,share=share)
        newBalance = token.balanceOf(vault)
        assert (oldBalance - newBalance) > share
        assert  newBalance >= vault.totalSupply()