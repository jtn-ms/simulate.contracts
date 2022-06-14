from brownie import StakingRewards, StakingToken, RewardToken
from brownie import accounts
from web3 import Web3

initial_supply = 1000000

signer = accounts[2]

# create token1
def deploy_ft_st():
    token = StakingToken.deploy(initial_supply, {'from': signer})
    print("Token0({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 

# create token2
def deploy_ft_rt():
    token = RewardToken.deploy(initial_supply, {'from': signer})
    print("Token1({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 

# create staking    
def deploy_staking(token0_addr, token1_addr):
    staking = StakingRewards.deploy(token0_addr,token1_addr, {'from': signer})
    print("Staking is deployed at {0} successfully.".format(staking.address))
    return staking

def main():
    token0 = deploy_ft_st()
    token1 = deploy_ft_rt()
    staking = deploy_staking(token0.address,token1.address)