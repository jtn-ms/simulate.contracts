
import pytest
from brownie import CPAMM, JTN, JNT
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
    amm = CPAMM.deploy(token0.address,token1.address, {'from': signer})
    print("AMM is deployed at {0} successfully.".format(amm.address))
    return amm

# @pytest.fixture(scope="module")
# def approve(token0,token1,amm,signer):
#     token0.approve(amm.address,10000, {'from': signer})
#     token1.approve(amm.address,10000, {'from': signer})

def test_approve(amm,signer,token0,token1):
    print("-----------APPROVE--------------")
    token0.approve(amm.address,10000, {'from': signer})
    token1.approve(amm.address,10000, {'from': signer})
        
def test_addLiquidity(amm,signer):
    token0in,token1in=100,100
    for i in range(3):
        _sharesTotal = amm.totalSupply()
        shares = amm.addLiquidity(token0in,token1in,{'from': signer}).return_value
        assert (shares + _sharesTotal) == amm.totalSupply()
        # assert amm.reserve0() == token0.balanceOf(amm.address)
        # assert amm.reserve1() == token1.balanceOf(amm.address)        

def test_swap0(amm,signer,token0,token1):
    tokenIn=100
    for i in range(2):
        tokenout = amm.swap(token0.address,tokenIn,{'from': signer}).return_value
        assert tokenIn > tokenout
        assert amm.reserve0() == token0.balanceOf(amm.address)
        assert amm.reserve1() == token1.balanceOf(amm.address)    

def test_swap1(amm,signer,token0,token1):
    tokenIn=100
    for i in range(2):
        tokenout = amm.swap(token1.address,tokenIn,{'from': signer}).return_value
        assert tokenIn > tokenout
        assert amm.reserve0() == token0.balanceOf(amm.address)
        assert amm.reserve1() == token1.balanceOf(amm.address)    
        
def test_removeLiquidity(amm,signer,token0,token1):
    shares = 100
    for i in range(3):
        _token0Reserve = token0.balanceOf(amm.address)
        _token1Reserve = token1.balanceOf(amm.address)  
        token0out,token1out = amm.removeLiquidity(shares,{'from': signer}).return_value
        assert amm.reserve0() == token0.balanceOf(amm.address)
        assert amm.reserve1() == token1.balanceOf(amm.address)
        assert (amm.reserve0() + token0out)== _token0Reserve
        assert (amm.reserve1() + token1out)== _token1Reserve