from random import random
from brownie import HDAirdrop, accounts, Contract

address_of_deployed_contract = ""
def main():
    factions = []
    n_mints = []
    accounts_to_airdrop_to = []
    account = accounts.load("hd_deployer")
    nft = HDAirdrop.at(address_of_deployed_contract)
    nft.partnerMint(factions, n_mints, accounts_to_airdrop_to, {"from": account})

