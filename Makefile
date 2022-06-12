# detect operating system
ifeq ($(OS),Windows_NT)
run.ganache:
	ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie

deploy.token:
	brownie.exe run .\scripts\deploy_Token.py

deploy.amm:
	brownie.exe run .\scripts\deploy_AMM.py

simulate.amm:
	brownie.exe run --silent .\scripts\simulate_AMM.py

simulate.compare:
	brownie.exe run --silent .\scripts\simulate_Compare.py

test.gas:
	brownie.exe test --gas

test:
	brownie.exe test

else
run.ganache:
	ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie

deploy.token:
	brownie run scripts/deploy_Token.py

deploy.amm:
	brownie run scripts/deploy_AMM.py

simulate.amm:
	brownie run --silent scripts/simulate_AMM.py

simulate.amm:
	brownie run --silent scripts/simulate_Compare.py

test.gas:
	brownie test --gas
endif