from brownie import Proxy, JTN, TestContract1, TestContract2, Helper
from brownie import accounts
from web3 import Web3

initial_supply = 1000000

signer = accounts[2]
randomUser = accounts[3]
x,y=10,20

def deploy():
    token = JTN.deploy(initial_supply, {'from': signer})
    proxy = Proxy.deploy({'from': signer})
    # t1 = TestContract1.deploy({'from': signer})
    # t2 = TestContract2.deploy(x,y,{'from': signer})
    helper = Helper.deploy({'from': signer})
    print("Token({0}) is deployed at {1} successfully.".format(token.name(),token.address))
    print("Proxy is deployed at {0} successfully.".format(proxy.address))
    # print("TestContract1 is deployed at {0} successfully.".format(t1.address))
    # print("TestContract1 is deployed at {0} successfully.".format(t2.address))
    print("Helper is deployed at {0} successfully.".format(helper.address))
    return token, proxy,helper

# ccode == callcode == contractcode   
def proxy_deploy(proxy,ccode,value=0):
    return proxy.deploy(ccode,{'from': signer,'value':value}).return_value

def proxy_execute(proxy,target,ccode,value=0):
    return proxy.execute(target,ccode,{'from': signer,'value':value}).return_value

def getByteCode_t1(helper):
    return helper.getBytecode1()#{'from': signer})

def getByteCode_t2(helper):
    return helper.getBytecode2(x,y)

def addr2bytes(addr):
    return "0"*24+addr[2:]

def main():
    token, proxy,helper = deploy()
    #print("ByteCode(TestContract1): {0}".format(getByteCode_t1(helper)))
    #print("ByteCode(TestContract2): {0}".format(getByteCode_t2(helper)))
    
    # deploy TestContract1
    bytecode="0x6080604052600080546001600160a01b0319163317905534801561002257600080fd5b50610151806100326000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c806313af40351461003b5780638da5cb5b14610050575b600080fd5b61004e6100493660046100eb565b61007f565b005b600054610063906001600160a01b031681565b6040516001600160a01b03909116815260200160405180910390f35b6000546001600160a01b031633146100c95760405162461bcd60e51b81526020600482015260096024820152683737ba1037bbb732b960b91b604482015260640160405180910390fd5b600080546001600160a01b0319166001600160a01b0392909216919091179055565b6000602082840312156100fd57600080fd5b81356001600160a01b038116811461011457600080fd5b939250505056fea26469706673582212201d0c8f5f01a52d4a12c7dd75b54496c0789344bcf366a8f08f12cf81ac1747a464736f6c634300080e0033"
    t1addr = proxy_deploy(proxy,bytecode)
    print("TestContract1 is deployed at {0} successfully".format(t1addr))
    # deploy TestContract2
    bytecode="0x60806040819052600080546001600160a01b031916331790553460015561014d3881900390819083398101604081905261003891610046565b60029190915560035561006a565b6000806040838503121561005957600080fd5b505080516020909101519092909150565b60d5806100786000396000f3fe6080604052348015600f57600080fd5b506004361060465760003560e01c80630c55699c14604b5780633fa4f2451460665780638da5cb5b14606e578063a56dfe4a146097575b600080fd5b605360025481565b6040519081526020015b60405180910390f35b605360015481565b6000546080906001600160a01b031681565b6040516001600160a01b039091168152602001605d565b60536003548156fea2646970667358221220565d6d684913e3fc77a90f13a879b7293aa47d943d827f340f82344f534902c764736f6c634300080e0033000000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000000000000000000000000000000000000000014"
    t2addr = proxy_deploy(proxy,bytecode)
    print("TestContract2 is deployed at {0} successfully".format(t2addr))
    
    # execute TestContract1
    # owner: 0x8da5cb5b
    # getOwner:893d20e8
    # x:0c55699c
    # 13af4035  =>  setOwner(address)
    print("owner: {0}".format(proxy.execute(t1addr,"0x8da5cb5b").return_value))
    proxy_execute(proxy,t1addr,"0x13af4035"+addr2bytes(randomUser.address))
    print("owner: {0}".format(proxy.execute(t1addr,"0x8da5cb5b").return_value))
    
    print("x: {0}".format(proxy.execute(t2addr,"0x0c55699c").return_value))