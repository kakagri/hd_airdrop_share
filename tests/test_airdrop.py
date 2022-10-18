from brownie import HDAirdrop, accounts, Contract
import brownie
import pytest


ipfs_pin = ""

def test_deployment():
    account = accounts[0]
    nft = HDAirdrop.deploy(ipfs_pin, {"from": account})

@pytest.fixture
def nft():
    account = accounts[0]
    nft = HDAirdrop.deploy(ipfs_pin, {"from": account})
    return nft

def test_mint(nft):
    account = accounts[0]
    airdrop_to = list([x.address for x in accounts[:5]])
    nft.mint(0, airdrop_to, {"from": account})
    for x in airdrop_to:
        amount = nft.balanceOf(x,0)
        assert amount == 1, f"address = {x}, amount = {amount}"


def test_set_base_uri(nft):
    account = accounts[0]
    nft.mint(0, [account.address], {"from": account})
    uri = nft.uri(0)
    assert uri == "", f"uri: {uri}"
    nft.setBaseURI("hello", {"from": account})
    uri = nft.uri(0)
    assert uri == "hello", f"uri: {uri}"


def test_multiple_mint():
    account = accounts[0]
    nft = HDAirdrop.deploy(ipfs_pin, {"from": account})
    airdrop_to = list([x.address for x in accounts[:5]])
    nft.mint(0, airdrop_to, {"from": account})
    nft.mint(0, airdrop_to, {"from": account})
    for x in airdrop_to:
        amount = nft.balanceOf(x,0)
        assert amount == 2, f"address = {x}, amount = {amount}"


def test_mint_from_other(nft):
    account = accounts[0]
    other_account = accounts[1]
    nft = HDAirdrop.deploy(ipfs_pin, {"from": account})
    airdrop_to = list([x.address for x in accounts[:5]])
    with brownie.reverts():
        nft.mint(0, airdrop_to, {"from": other_account})
    
def test_partner_mint(nft):
    account = accounts[0]
    airdrop_to = [accounts[k] for k in range(5)]
    amounts = [123, 12, 43, 900, 5739]
    factions = list(range(5))

    nft.partnerMint(factions, amounts, airdrop_to)
    
    for k in range(5):
        assert nft.balanceOf(accounts[k].address, k) == amounts[k]



