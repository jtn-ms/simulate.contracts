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

def deploy_ammEx(token0_addr, token1_addr):
    amm = NoReserveV.deploy(token0_addr,token1_addr, {'from': signer})
    print("NoReserveV AMM is deployed at {0} successfully.".format(amm.address))
    return amm

    
def main():   
    def query(token0,token1,amm):
        print("AMM.totalSupply: ",amm.totalSupply())
        print("AMM.reserve0: ",amm.reserve0())
        print("AMM.reserve1: ",amm.reserve1())
        print("token0.balanceOf(amm): ", token0.balanceOf(amm.address))   
        print("token1.balanceOf(amm): ", token1.balanceOf(amm.address))   
        print("amm.balanceOf(signer): ", amm.balanceOf(signer))

    def queryEx(token0,token1,amm,ammEx):
        print("amm|ammEx.totalSupply: {0}|{1}".format(amm.totalSupply(),ammEx.totalSupply()))
        print("amm.reserve0: {0}".format(amm.reserve0()))
        print("amm.reserve1: {0}".format(amm.reserve1()))
        print("token0.balanceOf(amm|ammEx): {0}|{1}".format(token0.balanceOf(amm.address),token0.balanceOf(ammEx.address)))
        print("token1.balanceOf(amm|ammEx): {0}|{1}".format(token1.balanceOf(amm.address),token1.balanceOf(ammEx.address)))
        print("amm|ammEx.balanceOf(signer): {0}|{1}".format(amm.balanceOf(signer),ammEx.balanceOf(signer)))
        
    def addLiquidity(amm,amount0=100,amount1=100):
        return amm.addLiquidity(amount0,amount1,{'from': signer})
        
    def removeLiquidity(amm,share=100):
        return amm.removeLiquidity(share,{'from': signer})

    def swap(amm,token,amount=100):
        return amm.swap(token.address,amount,{'from': signer})

    token0 = deploy_ft_jtn()
    token1 = deploy_ft_jnt()
    amm = deploy_amm(token0.address,token1.address)
    ammEx = deploy_ammEx(token0.address,token1.address)
    
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
        print("Get shares of {0} after depositing {1} {2} ".format(shares,token0in,token1in))
        print("Get shares of {0} after depositing {1} {2} ".format(sharesEx,token0in,token1in))
        queryEx(token0,token1,amm,ammEx)
        print("*******************************",i+1)
    
    print("---------SWAP--------------------")
    tokenin=100
    for i in range(4):
        tokenout = swap(amm,token0,amount=tokenin).return_value
        tokenoutEx = swap(ammEx,token0,amount=tokenin).return_value
        print("swap {0} token0 with {1} token1".format(tokenin,tokenout))
        print("swap {0} token0 with {1} token1".format(tokenin,tokenoutEx))
        queryEx(token0,token1,amm,ammEx)
        print("*******************************",i+1)
        
    
    print("---------REMOVE--------------------")
    shares = 100
    for i in range(6):
        token0out,token1out = removeLiquidity(amm,share=shares).return_value
        token0outEx,token1outEx = removeLiquidity(ammEx,share=shares).return_value
        print("Get {1} {2} at the cost of {0} shares".format(shares,token0out,token1out))
        print("Get {1} {2} at the cost of {0} shares".format(shares,token0outEx,token1outEx))
        queryEx(token0,token1,amm,ammEx)
        print("*******************************",i+1)
    