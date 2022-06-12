
import pytest
from brownie import CSAMM, JTN, JNT, NoReserveV
from brownie import accounts
from web3 import Web3

@pytest.fixture(scope="module")
def initial_supply():
    return 1000000

@pytest.fixture(scope="module")
def signer():
    return accounts[0]

# create token1
@pytest.fixture(scope="module")
def token0(initial_supply,signer):
    token = JTN.deploy(initial_supply, {'from': signer})
    print("Token0({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 

# create token2
@pytest.fixture(scope="module")
def token1(initial_supply,signer):
    token = JNT.deploy(initial_supply, {'from': signer})
    print("Token1({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 

# create amm   
@pytest.fixture(scope="module")
def amm(token0, token1,signer):
    amm = CSAMM.deploy(token0.address,token1.address, {'from': signer})
    print("AMM is deployed at {0} successfully.".format(amm.address))
    return amm

@pytest.fixture(scope="module")
def ammEx(token0, token1,signer):
    ammEx = NoReserveV.deploy(token0.address,token1.address, {'from': signer})
    print("NoReserveV AMM is deployed at {0} successfully.".format(ammEx.address))
    return ammEx

# @pytest.fixture(scope="module")
# def approve(token0, token1,amm, ammEx,signer):
#     print("-----------APPROVE------------------")
#     token0.approve(amm.address,10000, {'from': signer})
#     token1.approve(amm.address,10000, {'from': signer})
#     token0.approve(ammEx.address,10000, {'from': signer})
#     token1.approve(ammEx.address,10000, {'from': signer})  
          
def test_compare(amm,ammEx,signer,token0,token1):
    
    def addLiquidity(amm,amount0=100,amount1=100):
        return amm.addLiquidity(amount0,amount1,{'from': signer})
        
    def removeLiquidity(amm,share=100):
        return amm.removeLiquidity(share,{'from': signer})

    def swap(amm,token,amount=100):
        return amm.swap(token.address,amount,{'from': signer})

    def compare(token0,token1,amm,ammEx):
        assert amm.totalSupply() == ammEx.totalSupply()
        assert amm.reserve0() == token0.balanceOf(amm.address)
        assert amm.reserve1() == token1.balanceOf(amm.address)
        assert token0.balanceOf(amm.address) == token0.balanceOf(ammEx.address)
        assert token1.balanceOf(amm.address) == token1.balanceOf(ammEx.address)
        assert amm.balanceOf(signer) == ammEx.balanceOf(signer)
    
    
    print("-----------APPROVE------------------")
    token0.approve(amm.address,10000, {'from': signer})
    token1.approve(amm.address,10000, {'from': signer})
    token0.approve(ammEx.address,10000, {'from': signer})
    token1.approve(ammEx.address,10000, {'from': signer})  
        
    print("-----------ADD------------------")
    token0in,token1in=100,100
    for i in range(3):
        shares = addLiquidity(amm,amount0=token0in,amount1=token1in).return_value
        sharesEx = addLiquidity(ammEx,amount0=token0in,amount1=token1in).return_value
        compare(token0,token1,amm,ammEx)
    
    print("---------SWAP--------------------")
    tokenin=100
    for i in range(2):
        tokenout = swap(amm,token0,amount=tokenin).return_value
        tokenoutEx = swap(ammEx,token0,amount=tokenin).return_value
        compare(token0,token1,amm,ammEx)
    
    print("---------REMOVE--------------------")
    shares = 100
    for i in range(3):
        token0out,token1out = removeLiquidity(amm,share=shares).return_value
        token0outEx,token1outEx = removeLiquidity(ammEx,share=shares).return_value
        compare(token0,token1,amm,ammEx)

