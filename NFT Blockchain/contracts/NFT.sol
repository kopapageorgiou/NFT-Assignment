//SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract NFT is ERC721URIStorage, Ownable{
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    mapping(address => string) getOwnerOfaddress;
    constructor() ERC721("NFT", "ENEFTI"){}

    function mintNFT(address _signer, bytes memory _signature, string memory _fullname, string memory _uri) public returns (uint256){
        bytes32 dataHash = getMessageHash(_uri);
        bytes32 ethSignedDataHash = getEthSignedDataHash(dataHash);

        require(recover(ethSignedDataHash, _signature) == _signer, "Invalid signature");
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();
        _mint(_signer, newItemId);
        getOwnerOfaddress[_signer] = _fullname;
        _setTokenURI(newItemId, _uri);
        return newItemId;

    }
    function getNFT(uint256 _id) public view returns(string memory, string memory){
        string memory owner = getOwnerOfaddress[ownerOf(_id)];
        return (tokenURI(_id), owner);
    }

    function getCounter() public view returns(uint256){
        return _tokenIds.current();
    }

    function getMessageHash(string memory _data) public pure returns (bytes32){
        return keccak256(abi.encodePacked(_data));
    }

    function getEthSignedDataHash(bytes32 _dataHash) public pure returns (bytes32){
        return keccak256(abi.encodePacked(
            "\x19Ethereum Signed Message:\n32",
            _dataHash
        ));
    }

    function recover(bytes32 _ethSignedDataHash, bytes memory _signature) public pure returns (address) {
        (bytes32 r, bytes32 s, uint8 v) = _split(_signature);
        return ecrecover(_ethSignedDataHash, v, r, s);
    }

    function _split(bytes memory _signature) internal pure returns (bytes32 r, bytes32 s, uint8 v){
    
        require(_signature.length == 65, "Invalid signature length");

        assembly{
            r := mload(add(_signature, 32))
            s := mload(add(_signature, 64))
            v := byte(0, mload(add(_signature, 96)))
        }
    }
}