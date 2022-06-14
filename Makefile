# detect operating system
ifeq ($(OS),Windows_NT)
run.ganache:
	ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie


deploy:
	brownie.exe run .\scripts\deploy.py

simulate:
	brownie.exe run --silent .\scripts\simulate.py

test.gas:
	brownie.exe test --gas

test:
	brownie.exe test

else
run.ganache:
	ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie

deploy:
	brownie run scripts/deploy.py

simulate:
	brownie run --silent scripts/simulate.py

test.gas:
	brownie test --gas
endif