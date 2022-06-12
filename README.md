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
$ brownie run scripts/deploy_AMM.py
## simulate
$ brownie run scripts/simulate_AMM.py

# simulate on testnet
$ brownie run scripts/simulate_AMM.sol --network rinkeby

```
## Toolkits
- brownie
- ganache: ```ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie```
## Tech Stacks
- Web3
- ...

## Preassumption
- same value: value(token0) == value(token1)
- same amount input: token0in == token1in when **addLiquidity**(token0In,token1In)
- Expected output(constants): tokeOout = tokenIn * 997 / 1000 when **swap**(tokenIn)
- fails when expected tokenout > reserved tokenOut

## Gas Profiling ```brownie test --gas```
```
$ make test.gas
>>>
======================================= Gas Profile ======================================       

CPAMM <Contract>
   ├─ constructor     -  avg: 774716  avg (confirmed): 774716  low: 774716  high: 774716
   ├─ addLiquidity    -  avg: 133599  avg (confirmed): 133599  low: 104287  high: 192226
   ├─ swap            -  avg:  75897  avg (confirmed):  75897  low:  75875  high:  75943
   └─ removeLiquidity -  avg:  66451  avg (confirmed):  66451  low:  39871  high:  79741
JNT <Contract>
   ├─ constructor     -  avg: 634839  avg (confirmed): 634839  low: 634839  high: 634839
   └─ approve         -  avg:  44103  avg (confirmed):  44103  low:  44103  high:  44103
JTN <Contract>
   ├─ constructor     -  avg: 634839  avg (confirmed): 634839  low: 634839  high: 634839
   └─ approve         -  avg:  44103  avg (confirmed):  44103  low:  44103  high:  44103
```

## Results ```brownie run --silent scripts/simulate_AMM.py```
```
$ make simulate
>>>
Token0(JTN Token) is deployed at 0x0Bc0060Ae43892BE7E5Ce7eE6022Fc218d6418AA successfully.
Token1(JNT Token) is deployed at 0x7220d9FA0D2fBd790c081Eb5CB3301D728Ef42CC successfully.
AMM is deployed at 0x2F06Ef2B7E40520b0950E802586c04D4C9eD6Bea successfully.
-----------APPROVE------------------
-----------ADD------------------
Get shares of 100 after depositing 100 100 
Get shares of 100 after depositing 100 100 
Get shares of 100 after depositing 100 100 
---------SWAP--------------------
swap 100 token0 with 74 token1
swap 100 token0 with 44 token1
swap 100 token0 with 30 token1
---------REMOVE--------------------
Get 200 50 at the cost of 100 shares
Get 200 51 at the cost of 100 shares
Get 200 51 at the cost of 100 shares
---------SWAP--------------------
swap 100 token1 with 0 token0
swap 100 token1 with 0 token0
swap 100 token1 with 0 token0
-----------FINAL--------------------
AMM.totalSupply:  0
AMM.reserve0:  0
AMM.reserve1:  300
token0.balanceOf(amm):  0
token1.balanceOf(amm):  300
amm.balanceOf(signer):  0
```