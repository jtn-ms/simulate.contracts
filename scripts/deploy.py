from brownie import Proxy, JTN, TestContract1, TestContract2, Helper
from brownie import accounts
from web3 import Web3

initial_supply = 1000000

signer = accounts[2]
randomUser = accounts[3]

def deploy():
    token = JTN.deploy(initial_supply, {'from': signer})
    proxy = Proxy.deploy({'from': signer})
    t1 = TestContract1.deploy({'from': signer})
    t2 = TestContract2.deploy({'from': signer})
    helper = Helper.deploy({'from': signer})
    print("Token({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    print("Proxy is deployed at {0} successfully.".format(proxy.address))
    print("TestContract1 is deployed at {0} successfully.".format(t1.address))
    print("TestContract1 is deployed at {0} successfully.".format(t2.address))
    print("Helper is deployed at {0} successfully.".format(helper.address))
    return token, proxy,t1,t2,helper
    
def main():
    deploy()
    