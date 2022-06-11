## Contract Simulations & Get Insight Using Brownie
This project serves as a template to simulate kinds of complex solidity smart contracts and provide developers with the insight of its working.
Here, vault for yield farming is set as default. You can change it to whatever you want.
```
# preinstall
$ pip3 install package_name --user
$ python -m pip install --upgrade pip
$ pip install eth-brownie
$ npm install -g ganache-cli

# init project
$ brownie init

# set config file
# brownie-config.yaml, .env

# contracts & scripts

# compile
$ brownie compile

# deploy and/or simulate on localnet
$ brownie run scripts/deploy.py

# deploy and/or simulate on testnet
$ brownie run scripts/deploy_cornell_token.sol --network rinkeby

```
### Gas Profiling
```
$ make test.gas
>>>
==================================== Gas Profile ===================================== 

JTN <Contract>
   ├─ constructor -  avg: 634839  avg (confirmed): 634839  low: 634839  high: 634839
   └─ approve     -  avg:  44091  avg (confirmed):  44091  low:  44091  high:  44091
Vault <Contract>
   ├─ constructor -  avg: 336758  avg (confirmed): 336758  low: 336758  high: 336758
   ├─ deposit     -  avg:  69441  avg (confirmed):  69441  low:  61075  high: 102907
   └─ withdraw    -  avg:  46802  avg (confirmed):  46802  low:  26002  high:  52003
```
### Simulate
```
$ make simulate.vault
>>>
Token(JTN Token) is deployed at 0xD6cBE202Ca75b28c0A103Ae1B36bE0A56D26Cd14 successfully.
Vault is deployed at 0x4c22Af2d75f8Cb39c8F86D06155ae9c16BD459cC successfully.
-----------APPROVE------------------
-------signer2randomUser------------------
-------DEPOSIT<Indirect>(2Vault)--with 100 JTN
-----------DEPOSIT------------------
amount(in): 100, shares(out): 100
vault.totalSupply(shares) 100!=200 token.balanceOf(vault)
******************************* 1
amount(in): 100, shares(out): 50
vault.totalSupply(shares) 150!=300 token.balanceOf(vault)
******************************* 2
amount(in): 100, shares(out): 50
vault.totalSupply(shares) 200!=400 token.balanceOf(vault)
******************************* 3
amount(in): 100, shares(out): 50
vault.totalSupply(shares) 250!=500 token.balanceOf(vault)
******************************* 4
amount(in): 100, shares(out): 50
vault.totalSupply(shares) 300!=600 token.balanceOf(vault)
******************************* 5
---------WITHDRAW--------------------
shares(in): 100, amount(out): 200
vault.totalSupply(shares) 200!=400 token.balanceOf(vault)
******************************* 1
shares(in): 100, amount(out): 200
vault.totalSupply(shares) 100!=200 token.balanceOf(vault)
******************************* 2
shares(in): 100, amount(out): 200
vault.totalSupply(shares) 0==0 token.balanceOf(vault)
******************************* 3
```