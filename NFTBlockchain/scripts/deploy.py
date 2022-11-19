from brownie import NFT, accounts
from brownie.convert import to_address
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545", request_kwargs={'timeout':600}))
def main():
    #admin = accounts.load('papas')
    #admin = to_address("0xd376798453D13F3EB606B9FB83833ab664C5Cbc2")
    admin = web3.eth.accounts[0]
    deployed = NFT.deploy({
        "from": admin
    })
    

    #print(deployed)
    