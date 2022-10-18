from brownie import HDAirdrop, accounts, Contract


ipfs_pin = ""
def main():
    account = accounts.load("hd_deployer")
    nft = HDAirdrop.deploy(ipfs_pin, {"from": account}, publish_source = True)
