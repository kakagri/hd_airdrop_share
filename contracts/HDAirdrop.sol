// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/*
*Author: Khaled Grira 
*Human divergence airdrop of emblems
*/


contract HDAirdrop is ERC1155, Ownable, Pausable {
    string private baseURI;
    uint public constant MAX_FACTION = 5;


    constructor(string memory _baseURI) ERC1155(_baseURI)
    {
        baseURI = _baseURI;
    }

    function mint(uint _faction, address[] memory _whitelistedAddresses) 
        external
        onlyOwner
    {
        require(_faction < MAX_FACTION, "_faction out of range");
        for(uint k = 0; k < _whitelistedAddresses.length; k++) {
            _mint(_whitelistedAddresses[k], _faction, 1, "");
        }
    }

    function partnerMint(uint[] memory _factions, uint[] memory _nMints, address[] memory _addressesToAidropTo)
        external
        onlyOwner
    {
        require(_factions.length == _nMints.length && _factions.length == _addressesToAidropTo.length, "array lengths don't match");
        for(uint k = 0; k < _factions.length; k++) {
            require(_factions[k] < MAX_FACTION, "_faction out of range");
            _mint(_addressesToAidropTo[k], _factions[k], _nMints[k], "");
        }
    }

    function setBaseURI(string memory newURI)
        external
        onlyOwner
    {
        baseURI = newURI;
    }

    function uri(uint256) 
        public 
        view 
        virtual 
        override 
        returns (string memory) 
    {
        return baseURI;
    }
}


