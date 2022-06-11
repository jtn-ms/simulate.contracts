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
# shares/totalSupply == amount_in/token.balanceOf(address(this))
# if token.balanceOf(address(vault)) == vault.totalSupply
# shares == amount
# 
# [deposit]
# shares = (amount_in * totalSupply) / token.balanceOf(address(this));
# [withdraw]
# amount = (shares_out * token.balanceOf(address(this))) / totalSupply;
#
#

from brownie import CSAMM, JTN, JNT, accounts
from web3 import Web3

initial_supply = 1000000

signer = accounts[2]

# create token1
def deploy_ft_jtn():
    token = JTN.deploy(initial_supply, {'from': signer})
    print("Token({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    return token 

# create token2
def deploy_ft_jnt():
    token = JNT.deploy(initial_supply, {'from': signer})
    print("Token({0}) is deployed at {1} successfully.".format(token.name(),token.address))
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

def addLiquidity(amm,amount0=100,amount1=100):
    return amm.addLiquidity(amount0,amount1,{'from': signer})
    
def removeLiquidity(amm,share=100):
    return amm.removeLiquidity(share,{'from': signer})

def swap(amm,token,amount=100):
    return amm.swap(token.address,amount,{'from': signer})
    
def main():
    token0 = deploy_ft_jtn()
    token1 = deploy_ft_jnt()
    amm = deploy_amm(token0.address,token1.address)
    print("-----------APPROVE------------------")
    token0.approve(amm.address,10000, {'from': signer})
    token1.approve(amm.address,10000, {'from': signer})
    print("-----------ADD------------------")
    for i in range(3):
        shares = addLiquidity(amm,amount0=100,amount1=100)
        query(token0,token1,amm)
        print("*******************************")
    print("---------SWAP--------------------")
    for i in range(2):
        swap(amm,token0)
        query(token0,token1,amm)
        print("*******************************")
    print("---------REMOVE--------------------")
    for i in range(3):
        removeLiquidity(amm)
        query(token0,token1,amm)
        print("*******************************")
    