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
            with open(r'./NFTBlockchain/build/contracts/NFT.json', 'r') as fp:
                json_info = json.load(fp)
                abi = json_info['abi']
                self.account = config['SMART CONTRACT']['Default_Account']

                self.web3.eth.default_account = self.account
                self.contract = self.web3.eth.contract(address=address, abi=abi)
                print(self.account, self.contract)
        except:
            print('An error occured while loading abi from file')
        

    def mint(self, address: str, signature, uri: str, fullname: str):
        addr = self.web3.toChecksumAddress(address)
        txhash = self.contract.functions.mintNFT(addr, signature, uri, fullname).transact()
        receipt = self.web3.eth.wait_for_transaction_receipt(txhash)
        return receipt
    
    def getCurrentId(self):
        return self.contract.functions.getCounter().call()

    def transferEther(self, amount, to):
        nonce = self.web3.eth.getTransactionCount(self.account)
        key = "a29ff473fb15934bb3d04a7d7b6f355d034c20d4a04ea17fef281df596265783"
#build a transaction in a dictionary
        tx = {
            'nonce': nonce,
            'to': to,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        }

        #sign the transaction
        signed_tx = self.web3.eth.account.sign_transaction(tx, key)

        #send transaction
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        #get transaction hash
        print(self.web3.toHex(tx_hash))

    def getEthHash(self, message: str):
        h = self.contract.functions.getMessageHash(message).call()
        return self.contract.functions.getEthSignedDataHash(h).call()
    
    def getNFT(self, id: int):
        return self.contract.functions.getNFT(id).call()