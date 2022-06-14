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
$ brownie run scripts/deploy_Staking.py
## simulate
$ brownie run scripts/simulate_Staking.py

# simulate on testnet
$ brownie run scripts/simulate_Staking.sol --network rinkeby

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

StakingRewards <Contract>
   ├─ constructor     -  avg: 774716  avg (confirmed): 774716  low: 774716  high: 774716
   ├─ addLiquidity    -  avg: 133599  avg (confirmed): 133599  low: 104287  high: 192226
   ├─ swap            -  avg:  75897  avg (confirmed):  75897  low:  75875  high:  75943
   └─ removeLiquidity -  avg:  66451  avg (confirmed):  66451  low:  39871  high:  79741
RewardToken <Contract>
   ├─ constructor     -  avg: 634839  avg (confirmed): 634839  low: 634839  high: 634839
   └─ approve         -  avg:  44103  avg (confirmed):  44103  low:  44103  high:  44103
StakingToken <Contract>
   ├─ constructor     -  avg: 634839  avg (confirmed): 634839  low: 634839  high: 634839
   └─ approve         -  avg:  44103  avg (confirmed):  44103  low:  44103  high:  44103
```

## Results ```brownie run --silent scripts/simulate_Staking.py```
```
$ make simulate
>>>
Token0(Staking Token) is deployed at 0x147fb73B3CFa853cf9E047aD807099744832f87a successfully.
Token1(Reward Token) is deployed at 0x014Aab1ACc1A9Bb776F6c0805D21DF201494eE11 successfully.
Staking is deployed at 0x4D18a1B8E243138d602945482531197eA2218A72 successfully.
===========APPROVE===================
===========CHARGE(RewardToken)=======

===========BEGIN===================

-----------Stake------------------
Earned(0x0063): 0 
rewardPerToken: 0
Earned(0x0063): 0 
rewardPerToken: 0
Earned(0x0063): 100 
rewardPerToken: 500000000000000000
Earned(0x0063): 100 
rewardPerToken: 500000000000000000
Earned(0x0063): 100 
rewardPerToken: 500000000000000000

---------GetReward--------------------
Earned(0x0063): 0 
rewardPerToken: 833333333333333333

---------Withdraw--------------------
Earned(0x0063): 0 
rewardPerToken: 833333333333333333
Earned(0x0063): 100 
rewardPerToken: 1333333333333333333
Earned(0x0063): 100 
rewardPerToken: 1333333333333333333

===========FINAL====================
```