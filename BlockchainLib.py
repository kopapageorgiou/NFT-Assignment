from web3 import Web3
import json, configparser

class smartContract(object):

    def __init__(self, settings='settings.ini') -> None:
        
        config = configparser.ConfigParser()
        try:
            config.read(settings)
            addr = f"{config['SERVER']['Address']}:{config['SERVER']['Port']}"
            timeout = int(config['SERVER']['Timeout'])
        except:
            print('An error occured while reading config file')
        self.web3 = Web3(Web3.HTTPProvider(addr, request_kwargs={'timeout':timeout}))
        address = self.web3.toChecksumAddress(config['SMART CONTRACT']['Address'])

        try:
            with open(config['SMART CONTRACT']['Abi'], 'r') as fp:
                abi = json.load(fp)['abi']
        except:
            print('An error occured while loading abi from file')
        self.account = config['SMART CONTRACT']['Default_Account']

        self.web3.eth.default_account = self.account
        self.contract = self.web3.eth.contract(address=address, abi=abi)

    def mint(self, address: str, signature, uri: str, fullname: str):
        addr = self.web3.toChecksumAddress(address)
        txhash = self.contract.functions.mintNFT(addr, signature, uri, fullname).transact()
        receipt = self.web3.eth.wait_for_transaction_receipt(txhash)
        return receipt
    
    def getCurrentId(self):
        return self.contract.functions.getCounter().call()
