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
## deploy
$ brownie run scripts/deploy_vault.py
## simulate
$ brownie run scripts/simulate_AMM(SUM).py

# deploy and/or simulate on testnet
$ brownie run scripts/simulate_vault.sol --network rinkeby

```
## Toolkits
- brownie
- ganache: ```ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie```
## Tech Stacks
- Web3
- ...
## Results ```brownie run --silent scripts/simulate_AMM(SUM).py```

```
Token0(JTN Token) is deployed at 0x85FA27473554Dc7fe6007499f1942d3CF022d896 successfully.
Token1(JNT Token) is deployed at 0x1d467ABAa5116324a0a40f97ae569eF482e501f7 successfully.
AMM is deployed at 0x18cD7EA1780d9c59F09A6eED62F264e51f862C25 successfully.
-----------APPROVE------------------
-----------ADD------------------
Get shares of 200 after depositing 100 100 
AMM.totalSupply:  200
AMM.reserve0:  100
AMM.reserve1:  100
token0.balanceOf(amm):  100
token1.balanceOf(amm):  100
amm.balanceOf(signer):  200
******************************* 1
Get shares of 200 after depositing 100 100 
AMM.totalSupply:  400
AMM.reserve0:  200
AMM.reserve1:  200
token0.balanceOf(amm):  200
token1.balanceOf(amm):  200
amm.balanceOf(signer):  400
******************************* 2
Get shares of 200 after depositing 100 100 
AMM.totalSupply:  600
AMM.reserve0:  300
AMM.reserve1:  300
token0.balanceOf(amm):  300
token1.balanceOf(amm):  300
amm.balanceOf(signer):  600
******************************* 3
---------SWAP--------------------
swap 100 token0 with 99 token1
AMM.totalSupply:  600
AMM.reserve0:  400
AMM.reserve1:  201
token0.balanceOf(amm):  400
token1.balanceOf(amm):  201
amm.balanceOf(signer):  600
******************************* 1
swap 100 token0 with 99 token1
AMM.totalSupply:  600
AMM.reserve0:  500
AMM.reserve1:  102
token0.balanceOf(amm):  500
token1.balanceOf(amm):  102
amm.balanceOf(signer):  600
******************************* 2
---------REMOVE--------------------
Get 83 17 at the cost of 100 shares
AMM.totalSupply:  500
AMM.reserve0:  417
AMM.reserve1:  85
token0.balanceOf(amm):  417
token1.balanceOf(amm):  85
amm.balanceOf(signer):  500
******************************* 1
Get 83 17 at the cost of 100 shares
AMM.totalSupply:  400
AMM.reserve0:  334
AMM.reserve1:  68
token0.balanceOf(amm):  334
token1.balanceOf(amm):  68
amm.balanceOf(signer):  400
******************************* 2
Get 83 17 at the cost of 100 shares
AMM.totalSupply:  300
AMM.reserve0:  251
AMM.reserve1:  51
token0.balanceOf(amm):  251
token1.balanceOf(amm):  51
amm.balanceOf(signer):  300
******************************* 3
```