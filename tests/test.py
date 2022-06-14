import pytest
from brownie import Proxy, JTN
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
def proxy(signer):
    proxy = Proxy.deploy({'from': signer})
    return proxy

def test_clone(token,proxy,signer):
    pass