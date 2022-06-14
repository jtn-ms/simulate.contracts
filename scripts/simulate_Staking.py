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


 
# add stakes 
def staking_stake(staking,amount=100,cnt=3):
    print("\n-----------Stake------------------")
    
    for i in range(cnt):
        staking.stake(amount,{'from': signer})
        validate(staking)

# from brownie.convert import EthAddress

# remove stakes
def staking_withdraw(staking,amount=100,cnt=3):   
    print("\n---------Withdraw--------------------")
    
    for i in range(cnt):
        staking.withdraw(amount,{'from': signer})
        validate(staking)
# get rewards
def staking_getReward(staking,cnt=6):
    print("\n---------GetReward--------------------")
    staking.getReward()
    validate(staking)

# rewardPerTokenStored += (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / _totalSupply);
def staking_query_rewardPerToken(staking):
    return staking.rewardPerToken().return_value

# ((_balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
#            rewards[account]
def staking_query_earned(staking,account=signer):
    return staking.earned(account.address).return_value
    
def query(staking,account=signer,cnt=1):
    for i in range(cnt):
        earned = staking.earned(account.address, {'from': signer})
        rewardPerToken = staking.rewardPerToken({'from': signer})
        print("Earned({0}): {1} ".format(account.address[:6],earned))
        print("rewardPerToken: {0}".format(rewardPerToken))

def check(staking):
    pass

def validate(staking,printResult=True):
    if printResult:
        query(staking)
    else:
        check(staking)

def main():      
    stoken = deploy_ft_st()
    rtoken = deploy_ft_rt()
    staking = deploy_staking(stoken.address,rtoken.address)
    
    print("===========APPROVE===================")
    stoken.approve(staking.address,10000, {'from': signer})
    print("===========CHARGE(RewardToken)=======")
    rtoken.transfer(staking.address,10000, {'from': signer})

    print("\n===========BEGIN===================")
    staking_stake(staking,amount=100,cnt=3)
    query(staking,account=signer,cnt=2)
    staking_getReward(staking,cnt=3)
    staking_withdraw(staking,amount=100,cnt=3)
    print("\n===========FINAL====================")
    # query(token0,token1,staking)