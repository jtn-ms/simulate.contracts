
run.ganache:
	ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie

simulate.amm:
	brownie.exe run --silent scripts/simulate_AMM(SUM).py