
run.ganache:
	ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie

simulate.amm:
	brownie.exe run --silent scripts/simulate_AMM.py

test.consistency:
	brownie.exe test .\tests\test_amm.py

test.gas:
	brownie test --gas