### Instructions:
what you need to do in this order:

clone this repo
open a terminal and go into the folder 
run: brownie pm install Openzeppelin/openzeppelin-contracts@4.2.0

in scripts/.env -> fill the keys for etherscan, polygonscan and infura

generate an account in brownie on a secure laptop named "hd_deployer", send matic to it 
if you have the ipfs pin at that time fill it in scripts/deploy.py

to deploy run: brownie run scripts/deploy.py --network polygon-main

to change the ipfs pin: fill the ipfs pin in scripts/set_uri.py and run brownie run scripts/set_uri.py --network polygon-main

to airdrop 1 NFT per address: fill the factions and addresses in scripts/populate.py and run brownie run scripts/populate.py --network polygon-main

to airdrop to partners: fill the factions, n_mints, and address in scripts/airdrop_for_specific_address.py and run brownie run scripts/airdrop_for_specific_address.py --network polygon-main
