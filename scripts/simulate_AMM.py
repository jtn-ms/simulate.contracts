# [Share Section]
# uint public totalSupply;
# mapping(address => uint) public balanceOf;
# _mint()
# _burn() 
#
# [Liquidity Section]
# token = IERC20(_token);
#
# [BASE EQUATION]
# shares/totalSupply ==token0+1in/token0+1.balanceOf(address(this))
# if token.balanceOf(address(vault)) == vault.totalSupply
# shares == amount
# 
# [deposit]
# shares = (amount_in * totalSupply) / token.balanceOf(address(this));
# [withdraw]
# amount = (shares_out * token.balanceOf(address(this))) / totalSupply;
#
#

from brownie import CSAMM, JTN, JNT, NoReserveV
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
    amm = CSAMM.deploy(token0_addr,token1_addr, {'from': signer})
    print("AMM is deployed at {0} successfully.".format(amm.address))
    return amm

def query(token0,token1,amm):
    print("AMM.totalSupply: ",amm.totalSupply())
    print("AMM.reserve0: ",amm.reserve0())
    print("AMM.reserve1: ",amm.reserve1())
    print("token0.balanceOf(amm): ", token0.balanceOf(amm.address))   
    print("token1.balanceOf(amm): ", token1.balanceOf(amm.address))   
    print("amm.balanceOf(signer): ", amm.balanceOf(signer))
        
def check(token0,token1,amm):
    assert (amm.reserve0() + amm.reserve1()) >= amm.totalSupply()
    assert amm.reserve0() == token0.balanceOf(amm.address)
    assert amm.reserve1() == token1.balanceOf(amm.address)

def validate(token0,token1,amm,printResult=False):
    if printResult:
        query(token0,token1,amm)
    else:
        check(token0,token1,amm)
    
def amm_addLiquidity(amm,token0,token1,token0in=100,token1in=100,cnt=3):
    print("-----------ADD------------------")
    
    for i in range(cnt):
        shares =  amm.addLiquidity(token0in,token1in,{'from': signer}).return_value
        print("Get shares of {0} after depositing {1} {2} ".format(shares,token0in,token1in))
        validate(token0,token1,amm)
        # print("*******************************",i+1)

from brownie.convert import EthAddress

def amm_swap(amm,tokenIn,tokenOut,tokenin=100,cnt=3):   
    print("---------SWAP--------------------")
    
    iIdx,oIdx = (0,1) if EthAddress(tokenIn.address) == amm.token0() else (1,0)
    for i in range(cnt):
        tokenout = amm.swap(tokenIn.address,tokenin,{'from': signer}).return_value
        print("swap {0} token{2} with {1} token{3}".format(tokenin,tokenout,iIdx,oIdx))
        # print("*******************************",i+1)

def amm_removeLiquidity(amm,token0,token1,shares=100,cnt=6):        
    print("---------REMOVE--------------------")
    for i in range(cnt):
        token0out,token1out = amm.removeLiquidity(shares,{'from': signer}).return_value
        print("Get {1} {2} at the cost of {0} shares".format(shares,token0out,token1out))
        validate(token0,token1,amm)
        # print("*******************************",i+1)
                       
def main():      
    token0 = deploy_ft_jtn()
    token1 = deploy_ft_jnt()
    amm = deploy_amm(token0.address,token1.address)
    
    print("-----------APPROVE------------------")
    token0.approve(amm.address,10000, {'from': signer})
    token1.approve(amm.address,10000, {'from': signer})
    
    amm_addLiquidity(amm,token0,token1,token0in=100,token1in=100,cnt=3)
    amm_swap(amm,token0,token1,tokenin=100,cnt=3)
    amm_removeLiquidity(amm,token0,token1,shares=100,cnt=3)
    amm_swap(amm,token1,token0,tokenin=100,cnt=3)
    print("--------------FINAL----------------")
    query(token0,token1,amm)