# detect operating system
ifeq ($(OS),Windows_NT)
run.ganache:
	ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie

deploy.token:
	brownie.exe run .\scripts\deploy_SimpleToken.py

deploy.vault:
	brownie.exe run .\scripts\deploy_Vault.py

simulate.vault:
	brownie.exe run --silent .\scripts\simulate_vault.py

test.gas:
	brownie.exe test --gas

test:
	brownie.exe test

else
run.ganache:
	ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie

deploy.token:
	brownie run scripts/deploy_SimpleToken.py

deploy.vault:
	brownie run scripts/deploy_Vault.py

simulate.vault:
	brownie run --silent scripts/simulate_vault.py

test.gas:
	brownie test --gas
endif