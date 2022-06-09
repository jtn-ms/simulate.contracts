
run.ganache:
	ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie

# 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87
deploy.token:
	brownie.exe run .\scripts\deploy_MyToken.py

# 0x602C71e4DAC47a042Ee7f46E0aee17F94A3bA0B6
deploy.vault:
	brownie.exe run .\scripts\deploy_Vault.py

simulate.vault:
	brownie.exe run .\scripts\deploy_Vault.py