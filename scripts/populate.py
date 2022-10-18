from random import random
from brownie import HDAirdrop, accounts, Contract


ipfs_pin = ""
address_of_deployed_contract = ""
def main():
    accounts_to_airdrop_to = {}
    account = accounts.load("hd_deployer")
    nft = HDAirdrop.at(address_of_deployed_contract)
    for faction_number in accounts_to_airdrop_to:
        nft.mint(faction_number, accounts_to_airdrop_to[faction_number], {"from": account})
        print(f"done minting for faction: {faction_number}")

