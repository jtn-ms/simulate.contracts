
import pytest
from brownie import StakingRewards, StakingToken, RewardToken
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
    token = StakingToken.deploy(initial_supply, {'from': signer})
    print("Token0({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 

# create token2
@pytest.fixture(scope="module")
def token1(initial_supply,signer):
    token = RewardToken.deploy(initial_supply, {'from': signer})
    print("Token1({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 

# create staking   
@pytest.fixture(scope="module")
def staking(token0, token1,signer):
    staking = StakingRewards.deploy(token0.address,token1.address, {'from': signer})
    print("Staking is deployed at {0} successfully.".format(staking.address))
    return staking

# @pytest.fixture(scope="module")
# def approve(token0,token1,staking,signer):
#     token0.approve(staking.address,10000, {'from': signer})
#     token1.approve(staking.address,10000, {'from': signer})

def test_approve(staking,signer,token0,token1):
    print("-----------APPROVE--------------")
    token0.approve(staking.address,10000, {'from': signer})
    token1.approve(staking.address,10000, {'from': signer})
        
def test_addLiquidity(staking,signer):
    token0in,token1in=100,100
    for i in range(3):
        _sharesTotal = staking.totalSupply()
        shares = staking.addLiquidity(token0in,token1in,{'from': signer}).return_value
        assert (shares + _sharesTotal) == staking.totalSupply()
        # assert staking.reserve0() == token0.balanceOf(staking.address)
        # assert staking.reserve1() == token1.balanceOf(staking.address)        

def test_swap0(staking,signer,token0,token1):
    tokenIn=100
    for i in range(2):
        tokenout = staking.swap(token0.address,tokenIn,{'from': signer}).return_value
        assert tokenIn > tokenout
        assert staking.reserve0() == token0.balanceOf(staking.address)
        assert staking.reserve1() == token1.balanceOf(staking.address)    

def test_swap1(staking,signer,token0,token1):
    tokenIn=100
    for i in range(2):
        tokenout = staking.swap(token1.address,tokenIn,{'from': signer}).return_value
        assert tokenIn > tokenout
        assert staking.reserve0() == token0.balanceOf(staking.address)
        assert staking.reserve1() == token1.balanceOf(staking.address)    
        
def test_removeLiquidity(staking,signer,token0,token1):
    shares = 100
    for i in range(3):
        _token0Reserve = token0.balanceOf(staking.address)
        _token1Reserve = token1.balanceOf(staking.address)  
        token0out,token1out = staking.removeLiquidity(shares,{'from': signer}).return_value
        assert staking.reserve0() == token0.balanceOf(staking.address)
        assert staking.reserve1() == token1.balanceOf(staking.address)
        assert (staking.reserve0() + token0out)== _token0Reserve
        assert (staking.reserve1() + token1out)== _token1Reserve