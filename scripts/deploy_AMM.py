from brownie import CPAMM, JTN, JNT
from brownie import accounts
from web3 import Web3

initial_supply = 1000000

signer = accounts[2]

# create token1
def deploy_ft_jtn():
    token = JTN.deploy(initial_supply, {'from': signer})
    print("Token0({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 

# create token2
def deploy_ft_jnt():
    token = JNT.deploy(initial_supply, {'from': signer})
    print("Token1({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 

# create amm    
def deploy_amm(token0_addr, token1_addr):
    amm = CPAMM.deploy(token0_addr,token1_addr, {'from': signer})
    print("AMM is deployed at {0} successfully.".format(amm.address))
    return amm

def main():
    token0 = deploy_ft_jtn()
    token1 = deploy_ft_jnt()
    amm = deploy_amm(token0.address,token1.address)