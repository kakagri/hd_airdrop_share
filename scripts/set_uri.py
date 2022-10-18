from random import random
from brownie import HDAirdrop, accounts, Contract

address_of_deployed_contract = ""
ipfs_pin = ""
def main():
    account = accounts.load("hd_deployer")
    nft = HDAirdrop.at(address_of_deployed_contract)
    nft.setBaseURI(ipfs_pin, {"from": account})

